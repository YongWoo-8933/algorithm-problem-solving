"""
백준 23740 버스 노선 개편하기 (골드5)

1. 노선을 시작점 -> 끝점 순으로 정렬
2. 겹치는 부분을 확인하며 새 노선 추가(가장 적은 금액을 계속해서 갱신)
"""
from sys import stdin

N = int(stdin.readline())
lst = []
for i in stdin:
    S, E, C = map(int, i.split())
    lst.append((S, E, C))
lst.sort()
answer = [[lst[0][0], lst[0][1], lst[0][2]]]
for s, e, c in lst:
    if s<=answer[-1][1]:
        answer[-1][1] = max(answer[-1][1], e)
        answer[-1][2] = min(answer[-1][2], c)
    else:
        answer.append([s, e, c])
n = len(answer)
print(n)
for i in range(n):
    print(*answer[i])
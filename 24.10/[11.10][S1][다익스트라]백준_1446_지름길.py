"""
백준 1446 지름길 (실버1)

1. LIS(Longest Increasing Subsequence) 응용문제
2. 어떤 기둥을 하이라이트의 최하단으로 둘지 정함
3. 최하단 기둥을 기준으로 기둥의 오른쪽 왼쪽 방향 각각에 대해 LIS 알고리즘 실행
4. LIS 길이를 통해 최장 하이라이트 구간 산출
5 150
0 50 10
0 50 20
50 100 10
100 151 10
110 140 90
"""
from sys import stdin
from collections import deque

def main():
    _, goal = map(int, stdin.readline().split())
    lst = []
    for i in stdin:
        fr, to, cost = map(int, i.split())
        if to<=goal and cost<to-fr:
            lst.append((fr, to, cost))
    N = len(lst)
    lst.sort()
    q = deque([(0, 0, 0)])
    answer = 0
    while q:
        idx, total, pos = q.popleft()
        if idx==N:
            answer = max(answer, total)
            continue
        fr, to, cost = lst[idx]
        q.append((idx+1, total, pos))
        if fr>=pos:
            q.append((idx+1, total+to-fr-cost, to))
    print(goal-answer)

main()
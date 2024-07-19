"""
백준 15922 아우으 우아으이야!! (골드5)

1. 이전 구간에서 가장 큰 값을 p로 저장
2. 겹치는 부분을 제외하고 더해나감
"""
from sys import stdin

N = int(stdin.readline())
a, b = map(int, stdin.readline().split())
answer = b-a
p = b
for i in stdin:
    a, b = map(int, i.split())
    if p<=b:
        answer += b-max(a, p)
        p = b
print(answer)


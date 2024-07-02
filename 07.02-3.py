"""
백준 1715 카드 정렬하기 (골드4)

1. 가장 작은 카드 뭉치들부터 더해나가면 됨
2. 매 순간 가장 작은수의 카드뭉치를 찾기 위해 heapq 사용
3. heapq가 비었을때와 카드뭉치가 한개만 주어졌을때 예외처리 주의
"""
from sys import stdin
from heapq import heappush, heappop

N = int(stdin.readline())
hq = []
for i in stdin:
    heappush(hq, int(i))
answer = 0
if len(hq)==1:
    print(0)
    exit()
while hq:
    a, b = heappop(hq), heappop(hq)
    answer += a+b
    if hq:
        heappush(hq, a+b)
print(answer)


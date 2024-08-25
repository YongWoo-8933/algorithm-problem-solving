"""
백준 1922 네트워크 연결 (골드4)

1. 크루스칼 알고리즘 평범하게 돌리면 풀리는 문제(왜 골4인지 모르겠음)
"""
from sys import stdin, setrecursionlimit
from heapq import heappush, heappop

def find(x: int) -> int:
    global parents
    if parents[x]!=x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a: int, b: int):
    global parents
    ra, rb = find(a), find(b)
    if ra!=rb:
        parents[max(ra, rb)] = min(ra, rb)

setrecursionlimit(10**5)
N = int(stdin.readline())
V = int(stdin.readline())
q = []
for i in stdin:
    fr, to, cost = map(int, i.split())
    heappush(q, (cost, fr, to))

parents = [i for i in range(N+1)]
cnt, answer = 0, 0
while cnt<N-1:
    cost, fr, to = heappop(q)
    if find(fr)!=find(to):
        cnt += 1
        answer += cost
        union(fr, to)
print(answer)


"""
백준 1766 문제집

1. 위상정렬 + 우선순위큐를 사용하면 쉽게 풀림
2. 일반적인 위상정렬 알고리즘에서, q를 우선순위큐로 사용
"""
from sys import stdin
from heapq import heappop, heappush
N, M = map(int, stdin.readline().split())
links = [set() for _ in range(N+1)]
indegrees = [0]*(N+1)
for i in stdin:
    fr, to = map(int, i.split())
    links[fr].add(to)
    indegrees[to] += 1

q = []
for i in range(1, N+1):
    if indegrees[i]==0:
        heappush(q, i)
answer = []
while q:
    node = heappop(q)
    answer.append(node)
    for next_node in links[node]:
        indegrees[next_node] -= 1
        if indegrees[next_node]==0:
            heappush(q, next_node)

print(*answer)










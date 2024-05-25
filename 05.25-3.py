"""
백준 2252 줄 세우기

1. 위상정렬 알고리즘 구현
2. 전형적인 위상 정렬 알고리즘대로 진행한 후 q에서 pop되는 node 순서대로 배열에 저장, 출력
"""
from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
heights = [set() for _ in range(N+1)]
indegree = [0] * (N+1)
for i in stdin:
    small, tall = map(int, i.split())
    heights[small].add(tall)
    indegree[tall] += 1
q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)
answer = []
while q:
    node = q.popleft()
    answer.append(node)
    for next_node in heights[node]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            q.append(next_node)
print(*answer)
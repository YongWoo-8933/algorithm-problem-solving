"""
백준 1005 ACM Craft (골드3)

1. 위상정렬 알고리즘을 활용
2. dp table을 운영해, 각 노드까지의 최소 빌드시간을 기록
"""
from sys import stdin
from collections import deque

input = stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())
    times = [0, *map(int, input().split())]
    graph = [set() for _ in range(N+1)]
    indegree = [0] * (N+1)
    for _ in range(K):
        fr, to = map(int, input().split())
        graph[fr].add(to)
        indegree[to] += 1
    target = int(input())
    q = deque()
    dp = times.copy()
    for i in range(1, N+1): 
        if indegree[i] == 0:
            q.append(i)
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            indegree[next_node] -= 1
            dp[next_node] = max(dp[next_node], dp[node]+times[next_node])
            if indegree[next_node] == 0:
                q.append(next_node)
    print(dp[target])
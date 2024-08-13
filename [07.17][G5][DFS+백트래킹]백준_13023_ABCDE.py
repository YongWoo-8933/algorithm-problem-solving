"""
백준 13023 ABCDE (골드5)

1. 5개의 노드를 방문하는 즉시 프로그램을 종료하면 되므로 dfs가 적합
2. 모든 노드를 시점으로 dfs를 실행해 하나라도 조건을 만족하는게 있다면 1 리턴
3. visited table은 하나만 운영하고, 백트래킹 형식으로 값을 변경해가며 진행
"""
from sys import stdin

def dfs(cnt: int, node: int):
    global visited
    if cnt==5:
        print(1)
        exit()
    for next_node in friends[node]:
        if not visited[next_node]:
            visited[next_node] = 1
            dfs(cnt+1, next_node)
            visited[next_node] = 0

N, M = map(int, stdin.readline().split())
friends = [set() for _ in range(N)]
for i in stdin:
    a, b = map(int, i.split())
    friends[a].add(b)
    friends[b].add(a)

visited = [0]*N
for start_node in range(N):
    visited[start_node] = 1
    dfs(1, start_node)
    visited[start_node] = 0
print(0)


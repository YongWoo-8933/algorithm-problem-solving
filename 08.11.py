"""
백준 22869 징검다리 건너기 (small) (실버 1)

1. 완전탐색으로 건널수 있는 다리를 하나씩 체크
2. 이때 멀리 가있는 node부터 검사함으로써 연산을 줄임
"""
import sys

def dfs(node: int):
    global lst, visited, N, K
    if node==N-1:
        print("YES")
        exit()
    for next_node in range(node+K, node, -1):
        if next_node<N and (next_node-node)*(1+abs(lst[next_node]-lst[node]))<=K and not visited[next_node]:
            visited[next_node] = True
            dfs(next_node)

sys.setrecursionlimit(10**5)
N, K = map(int, input().split())
lst = [*map(int, input().split())]
visited = [False]*N
visited[0] = True
dfs(0)
print("NO")


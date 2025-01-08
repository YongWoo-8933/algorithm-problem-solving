"""
백준 13700 완전범죄 (실버1)

1. BFS로 이동하며 탈출하는 경우를 찾아내면 됨.
"""

from collections import deque

def main():
    N, S, D, F, B, K = map(int, input().split())
    police_offices = set()
    if K:
        police_offices = { *map(int, input().split()) }
    q = deque([(0, S)])
    visited = [False]*(N+1)
    visited[S] = True
    while q:
        cnt, node = q.popleft()
        if node in police_offices:
            continue
        if node==D:
            print(cnt)
            exit()
        for next_node in [node+F, node-B]:
            if 0<next_node<=N and not visited[next_node]:
                visited[next_node] = True
                q.append((cnt+1, next_node))
    print("BUG FOUND")

main()
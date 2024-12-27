"""
백준 2644 촌수계산(실버2)

1. 연결관계 정리 후 BFS로 두 노드간 거리 계산
"""
from sys import stdin
from collections import deque

def main():
    N = int(stdin.readline())
    a, b = map(int, stdin.readline().split())
    stdin.readline()
    links = [set() for _ in range(N+1)]
    for i in stdin:
        parent, child = map(int, i.split())
        links[parent].add(child)
        links[child].add(parent)
    q = deque([(0, a)])
    visited = [False]*(N+1)
    visited[a] = True
    while q:
        cnt, node = q.popleft()
        if node==b:
            print(cnt)
            break
        for next_node in links[node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append((cnt+1, next_node))
    else:
        print(-1)
main()

"""
백준 18352 특정 거리의 도시 찾기 (실버2)

1. 딱 K번째 길이까지만 BFS 진행
"""
from sys import stdin
from collections import deque

def main():
    N, _, K, X = map(int, stdin.readline().split())
    links = [set() for _ in range(N+1)]
    for i in stdin:
        fr, to = map(int, i.split())
        links[fr].add(to)
    visited = [False]*(N+1)
    visited[X] = True
    q = deque([(0, X)])
    answer = []
    while q:
        length, node = q.popleft()
        if length==K:
            answer.append(node)
            continue
        for next_node in links[node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append((length+1, next_node))
    answer.sort()
    if answer:
        print(*answer)
    else:
        print(-1)

main()
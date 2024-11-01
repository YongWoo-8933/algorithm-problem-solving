"""
백준 2458 키순서 (골드4)

1. BFS로 두번 돌리면 간단히 끝남
2. 시간 복잡도를 줄이려면 간단한 메모제이션을 추가해주면 됨
"""

from sys import stdin
from collections import deque

def main():
    N, _ = map(int, stdin.readline().split())
    ascending = [set() for _ in range(N+1)]
    for i in stdin:
        small, tall = map(int, i.split())
        ascending[small].add(tall)
    smaller = [set() for _ in range(N+1)]
    taller = [0 for _ in range(N+1)]
    for start_node in range(1, N+1):
        visited = [False for _ in range(N+1)]
        visited[start_node] = True
        q = deque([start_node])
        taller_cnt = 0
        while q:
            node = q.popleft()
            for next_node in ascending[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    taller_cnt += 1
                    smaller[next_node].add(start_node)
                    q.append(next_node)
        taller[start_node] = taller_cnt
    answer = 0
    for node in range(1, N+1):
        if len(smaller[node])+taller[node]+1==N:
            answer += 1
    print(answer)
main()
"""
백준 4485 녹색 옷 입은 애가 젤다지? (골드4)

1. 평범한 다익스트라 알고리즘 구현하면 됨
"""
from sys import stdin
from heapq import heappush, heappop

problem_N = 1
while N := int(stdin.readline()):
    MAP = [[*map(int, stdin.readline().split())] for _ in range(N)]
    visited = [[2500]*N for _ in range(N)]
    visited[0][0] = MAP[0][0]
    hq = [(MAP[0][0], 0, 0)]
    while hq:
        cost, row, col = heappop(hq)
        if row==N-1 and col==N-1:
            print(f"Problem {problem_N}: {cost}")
            break
        for nrow, ncol in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
            if 0<=nrow<N and 0<=ncol<N and cost+MAP[nrow][ncol]<visited[nrow][ncol]:
                visited[nrow][ncol] = cost+MAP[nrow][ncol]
                heappush(hq, (cost+MAP[nrow][ncol], nrow, ncol))
    problem_N += 1


"""
백준 1600 말이 되고픈 원숭이 (골드3)

1. 남은 K횟수에 따른 visited table을 만들어놓고 BFS진행하면 됨
2. 각 이동시 k가 남아있다면 말이동하는 경우까지 q에 추가
"""
from sys import stdin
from collections import deque

def bfs():
    global K, W, H, MAP
    q = deque([(0, K, 0, 0)])
    visited = [[[False]*(K+1) for __ in range(W)] for _ in range(H)]
    visited[0][0][K] = True
    while q:
        cnt, k, row, col = q.popleft()
        if row==H-1 and col==W-1:
            return cnt
        # 그냥 이동
        for nrow, ncol in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0<=nrow<H and 0<=ncol<W and MAP[nrow][ncol]==0 and not visited[nrow][ncol][k]:
                visited[nrow][ncol][k] = True
                q.append((cnt+1, k, nrow, ncol))
        # 말처럼 이동
        if k:
            for nrow, ncol in [(row-1, col-2), (row-2, col-1), (row-2, col+1), (row-1, col+2),
                            (row+1, col-2), (row+2, col-1), (row+2, col+1), (row+1, col+2)]:
                if 0<=nrow<H and 0<=ncol<W and MAP[nrow][ncol]==0 and not visited[nrow][ncol][k-1]:
                    visited[nrow][ncol][k-1] = True
                    q.append((cnt+1, k-1, nrow, ncol))
    return -1

K = int(stdin.readline())
W, H = map(int, stdin.readline().split())
MAP = [[*map(int, i.split())] for i in stdin]
print(bfs())

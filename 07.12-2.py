"""
백준 2636 치즈 (골드4)

13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0

3
5
"""
from sys import stdin
from collections import deque

H, W = map(int, stdin.readline().split())
# MAP = [[*map(int, i.split())] for i in stdin]
MAP = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
day = 0
while sum(sum(MAP[i]) for i in range(H)):
    answer = 0
    visited = [[0]*W for _ in range(H)]
    visited[0][0] = 1
    q = deque([(0, 0)])
    while q:
        row, col = q.popleft()
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nrow, ncol = row+dy, col+dx
            if 0<=nrow<H and 0<=ncol<W and not visited[nrow][ncol]:
                visited[nrow][ncol] = 1
                if MAP[nrow][ncol]==0:
                    q.append((nrow, ncol))
                elif MAP[nrow][ncol]==1:
                    MAP[nrow][ncol] = 2
    for row in range(H):
        for col in range(W):
            if MAP[row][col]==2:
                answer += 1
                MAP[row][col] = 0
    day += 1
print(day, answer)

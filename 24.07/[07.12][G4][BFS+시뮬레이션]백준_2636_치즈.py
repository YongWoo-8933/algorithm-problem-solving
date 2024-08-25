"""
백준 2636 치즈 (골드4)

1. (0, 0)에서부터 BFS를 돌려 외부 공기부분만 체크하도록 함
2. 외부 공기에 접한 치즈가 있다면 마킹(1 -> 2)
3. 마킹한 치즈를 없앰(2 -> 0)
4. 모든 값이 0이면 루프를 종료하고 day 리턴
"""
from sys import stdin
from collections import deque

H, W = map(int, stdin.readline().split())
MAP = [[*map(int, i.split())] for i in stdin]
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

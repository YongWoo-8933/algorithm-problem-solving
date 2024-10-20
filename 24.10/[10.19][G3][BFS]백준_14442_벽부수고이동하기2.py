"""
백준 14442 벽 부수고 이동하기 2 (골드3)

1. visited를 체크할때 이동한 거리를 저장하는게 아니라 부순 벽의 횟수를 저장하는게 포인트
2. 해당 칸에 나중에 도달했더라도, 벽을 부순 횟수가 적다면 bfs가 진행된다는 점을 이용 
"""

from sys import stdin
from collections import deque

H, W, K = map(int, stdin.readline().split())
MAP = [i.strip() for i in stdin]
max_use = 2000
visited = [[max_use]*W for __ in range(H)]
q = deque([(1, 0, 0)])
visited[0][0] = 0
while q:
    cnt, row, col = q.popleft()
    if row==H-1 and col==W-1:
        print(cnt)
        exit()
    for nrow, ncol in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
        if 0<=nrow<H and 0<=ncol<W:
            next_use = visited[row][col] + int(MAP[nrow][ncol])
            if next_use<=K and next_use<visited[nrow][ncol]:
                visited[nrow][ncol] = next_use
                q.append((cnt+1, nrow, ncol))
print(-1)

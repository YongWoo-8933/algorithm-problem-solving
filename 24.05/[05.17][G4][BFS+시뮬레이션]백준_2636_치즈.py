"""
백준 치즈 (골드4)

1. 매 시간마다 외부공기 마킹 -> 인접치즈 녹이기
"""
from sys import stdin
from collections import deque

H, W = map(int, stdin.readline().split())
MAP = [[*map(int, i.split())] for i in stdin]
hours = 0
while any([any(j==1 for j in MAP[i]) for i in range(H)]):
    hours += 1
    # 외부공기 구분용 BFS
    start_row, start_col = -1, -1
    for i in [0, H-1]:
        for j in range(W):
            if MAP[i][j] == 0:
                start_row, start_col = i, j
    for j in [0, W-1]:
        for i in range(H):
            if MAP[i][j] == 0:
                start_row, start_col = i, j
    q = deque([(start_row, start_col)])
    external_area = [[0]*W for _ in range(H)]
    external_area[start_row][start_col] = 1
    while q:
        row, col = q.popleft()
        for dx, dy in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            new_row, new_col = row+dy, col+dx
            if 0<=new_row<H and 0<=new_col<W and MAP[new_row][new_col]==0 and external_area[new_row][new_col]==0:
                external_area[new_row][new_col] = 1
                q.append((new_row, new_col))
    # 접한 치즈 녹이기
    for i in range(H):
        for j in range(W):
            if MAP[i][j] == 1:
                count = 0
                for dx, dy in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
                    new_i, new_j = i+dy, j+dx
                    if 0<=new_i<H and 0<=new_j<W and external_area[new_i][new_j]:
                        count += 1
                if count >= 2:
                    MAP[i][j] = 0
print(hours)

    


"""
백준 20057 마법사 상어와 토네이도 (골드3)

1. 방향에따라 모래가 퍼지는 위치와 비율을 미리 정의
2. 토네이도 방향이 바뀌는 대각선에 있다면 방향 바꾸기
3. 이후 시뮬레이션 진행
"""

from sys import stdin
from collections import deque

def main():
    N = int(stdin.readline())
    MAP = [[*map(int, i.split())] for i in stdin]
    spread_ratio = [
        # 좌
        [(-1, 0, 0.07), (1, 0, 0.07), (-2, 0, 0.02), (2, 0, 0.02), (0, -2, 0.05), 
         (-1, -1, 0.1), (1, -1, 0.1), (-1, 1, 0.01), (1, 1, 0.01)],
        # 하
        [(0, -1, 0.07), (0, 1, 0.07), (0, 2, 0.02), (0, -2, 0.02), (2, 0, 0.05), 
         (1, -1, 0.1), (1, 1, 0.1), (-1, -1, 0.01), (-1, 1, 0.01)],
        # 우
        [(-1, 0, 0.07), (1, 0, 0.07), (-2, 0, 0.02), (2, 0, 0.02), (0, 2, 0.05), 
         (-1, 1, 0.1), (1, 1, 0.1), (-1, -1, 0.01), (1, -1, 0.01)],
        # 상
        [(0, -1, 0.07), (0, 1, 0.07), (0, 2, 0.02), (0, -2, 0.02), (-2, 0, 0.05), 
         (-1, -1, 0.1), (-1, 1, 0.1), (1, -1, 0.01), (1, 1, 0.01)],
    ]
    d_yx = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    q = deque([(0, N//2, N//2-1)])
    answer = 0
    while q:
        direction, row, col = q.popleft()
        if row==0 and col==-1:
            break
        sand_remain = MAP[row][col]
        for dy, dx, ratio in spread_ratio[direction]:
            nrow, ncol = row+dy, col+dx
            spreaded_sand = int(MAP[row][col]*ratio)
            sand_remain -= spreaded_sand
            if 0<=nrow<N and 0<=ncol<N:
                MAP[nrow][ncol] += spreaded_sand
            else:
                answer += spreaded_sand
        dy, dx = d_yx[direction]
        nrow, ncol = row+dy, col+dx
        if 0<=nrow<N and 0<=ncol<N:
            MAP[nrow][ncol] += sand_remain
        else:
            answer += sand_remain
        new_direction = direction
        if row==N-col-1 or (row<=N//2 and row-1==col) or (N//2<row and row==col):
            new_direction += 1
            new_direction %= 4
        dy, dx = d_yx[new_direction]
        q.append((new_direction, row+dy, col+dx))
    print(answer)
main()
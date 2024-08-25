"""
백준 15685 드래곤 커브 (골드3)

1. 드래곤 커브를 이루는 모든 점들의 경로를 lst 형태로 저장
2. 각 리스트의 마지막 점을 기준으로(끝점) 이전 점들에 대해 
   거꾸로 회전을 적용해 리스트에 추가
3. 추가된 점들을 board에 하나씩 체크
4. 체크된 board를 기반으로 모든 점을 순회하며 정사각형의 갯수 출력
"""
from sys import stdin

N = int(stdin.readline())
board = [[False]*101 for _ in range(101)]
d_xy = [(1, 0), (0, -1), (-1, 0), (0, 1)]
for i in stdin:
    x, y, d, g = map(int, i.split())
    nx, ny = x+d_xy[d][0], y+d_xy[d][1]
    cur_points = [(x, y), (nx, ny)]
    cur_g = 0
    board[y][x] = True
    board[ny][nx] = True
    while cur_g<g:
        ex, ey = cur_points[-1]
        n = len(cur_points)
        for i in range(n-2, -1, -1):
            px, py = cur_points[i]
            nx, ny = ex+ey-py, ey-ex+px
            board[ny][nx] = True
            cur_points.append((nx, ny))
        cur_g += 1
answer = 0
for y in range(100):
    for x in range(100):
        if board[y][x] and board[y+1][x] and board[y][x+1] and board[y+1][x+1]:
            answer += 1
print(answer)

    


"""
백준 14503 로봇 청소기(골드 5)

1. 주어진 조건대로 순서에 유의하여 구현하면 됨
2. 주변에 청소할 곳이 있다면 우선 방향전환부터 시작한다는게 포인트
3. 우선 방향전환을 4번 한 뒤, 청소할 곳이 없다면 그다음을 진행하는게 로직상 편함
"""
from sys import stdin

H, W = map(int, stdin.readline().split())
srow, scol, sdir = map(int, stdin.readline().split())
board = [[*map(int, i.split())] for i in stdin]
row, col, d = srow, scol, sdir
d_yx = [(-1, 0), (0, 1), (1, 0), (0, -1)]
while 1:
    if board[row][col]==0:
        board[row][col] = 2
    nd = d
    movable = False
    for _ in range(4):
        nd -= 1
        nd %= 4
        dy, dx = d_yx[nd]
        nrow, ncol = row+dy, col+dx
        if 0<=nrow<H and 0<=ncol<W and board[nrow][ncol]==0:
            movable = True
            break
    if movable:
        row, col, d = nrow, ncol, nd
    else:
        dy, dx = d_yx[(d+2)%4]
        nrow, ncol = row+dy, col+dx
        if 0<=nrow<H and 0<=ncol<W and board[nrow][ncol]!=1:
            row, col = nrow, ncol
        else:
            break
print(sum(i.count(2) for i in board))
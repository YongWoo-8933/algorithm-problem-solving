"""
백준 3190 뱀 (골드4)

* 시키는대로 매 초마다 뱀의 이동을 구현하면 됨
주의할점
1. 뱀의 이동 경로를 기억해 꼬리를 없애는 부분
2. 방향전환
"""
from sys import stdin
from collections import deque

N, K = int(stdin.readline()), int(stdin.readline())
board = [[0]*N for _ in range(N)]
for _ in range(K):
    r, c = map(int, stdin.readline().split())
    board[r-1][c-1] = 1
commands = [""]*10001
for _ in range(int(stdin.readline())):
    x, command = stdin.readline().strip().split()
    commands[int(x)] = command

# 우 하 좌 상 -> 0 1 2 3
t = 0
snake_route, d = deque([(0, 0)]), 0
dyx = [(0, 1), (1, 0), (0, -1), (-1, 0)]
board[0][0] = -1
while 1:
    t += 1
    dy, dx = dyx[d]
    head_row, head_col = snake_route[-1]
    nrow, ncol = head_row+dy, head_col+dx
    if 0<=nrow<N and 0<=ncol<N and board[nrow][ncol]!=-1:
        snake_route.append((nrow, ncol))
        if board[nrow][ncol]==0:
            tail_row, tail_col = snake_route.popleft()
            board[tail_row][tail_col] = 0
        board[nrow][ncol] = -1
    else:
        print(t)
        break
    if t<10001 and commands[t]:
        d += [-1, 1][commands[t]=="D"]
        d %= 4



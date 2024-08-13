"""
백준 13460 구슬탈출2

1. 상/하/좌/우로 구슬이 이동할때 파란색/빨간색 구슬을 따로 움직여줌
2. 구슬이 이동하는 도중 반대색 구슬을 만났다면, 최종 위치에서 한칸 덜 감
3. 어떤 경우에도 파란색 구슬의 이동경로에 O가 있다면 종료
4. 파란색 구슬이 O를 만나지 않고 빨간색 구슬이 O를 만날때만 카운트
5. 4^10가지 모든 경우를 따지면 시간초과가 나므로, 빨간색 구슬이 도착한 경우가 있다면
   answer를 갱신하고, 이후 answer보다 많은 횟수를 진행한 모든 경우는 종료
6. 1~5에 유의한 재귀 알고리즘 구성
"""
from sys import stdin
from copy import deepcopy

def move_ball(board: list, direction: int, row: int, col: int) -> tuple:
    is_behind = False
    if direction==0:
        # 상
        current = row
        while 1:
            current -= 1
            if board[current][col]=="#":
                return (False, current+1+[0,1][is_behind], col)
            elif board[current][col]=="O":
                return (True, current, col)
            elif board[current][col] in "BR":
                is_behind = True
    elif direction==1:
        # 하
        current = row
        while 1:
            current += 1
            if board[current][col]=="#":
                return (False, current-1-[0,1][is_behind], col)
            elif board[current][col]=="O":
                return (True, current, col)
            elif board[current][col] in "BR":
                is_behind = True
    elif direction==2:
        # 좌
        current = col
        while 1:
            current -= 1
            if board[row][current]=="#":
                return (False, row, current+1+[0,1][is_behind])
            elif board[row][current]=="O":
                return (True, row, current)
            elif board[row][current] in "BR":
                is_behind = True
    elif direction==3:
        # 우
        current = col
        while 1:
            current += 1
            if board[row][current]=="#":
                return (False, row, current-1-[0,1][is_behind])
            elif board[row][current]=="O":
                return (True, row, current)
            elif board[row][current] in "BR":
                is_behind = True

def tilt(board: list, red_coord: list, blue_coord: list, direction: int) -> tuple:
    blue_ball_in_hole, n_blue_row, n_blue_col = move_ball(board, direction, blue_coord[0], blue_coord[1])
    if blue_ball_in_hole:
        return False, True, [], []
    
    red_ball_in_hole, n_red_row, n_red_col = move_ball(board, direction, red_coord[0], red_coord[1])
    if red_ball_in_hole:
        return True, False, [], []
    
    return False, False, [n_red_row, n_red_col], [n_blue_row, n_blue_col]
    
def f(cnt: int, board: list, red_coord: list, blue_coord: list):
    global answer
    if cnt<10 and cnt<answer:
        # 상
        if board[red_coord[0]-1][red_coord[1]] in ".O" or board[blue_coord[0]-1][blue_coord[1]] in ".O":
            red_ball_in_hole, blue_ball_in_hole, n_red_coord, n_blue_coord = tilt(board, red_coord, blue_coord, 0)
            if red_ball_in_hole:
                answer = min(answer, cnt+1)
            elif not blue_ball_in_hole:
                t_board = deepcopy(board)
                t_board[red_coord[0]][red_coord[1]] = "."
                t_board[n_red_coord[0]][n_red_coord[1]] = "R"
                t_board[blue_coord[0]][blue_coord[1]] = "."
                t_board[n_blue_coord[0]][n_blue_coord[1]] = "B"
                f(cnt+1, t_board, n_red_coord, n_blue_coord)
        # 하
        if board[red_coord[0]+1][red_coord[1]] in ".O" or board[blue_coord[0]+1][blue_coord[1]] in ".O":
            red_ball_in_hole, blue_ball_in_hole, n_red_coord, n_blue_coord = tilt(board, red_coord, blue_coord, 1)
            if red_ball_in_hole:
                answer = min(answer, cnt+1)
            elif not blue_ball_in_hole:
                t_board = deepcopy(board)
                t_board[red_coord[0]][red_coord[1]] = "."
                t_board[n_red_coord[0]][n_red_coord[1]] = "R"
                t_board[blue_coord[0]][blue_coord[1]] = "."
                t_board[n_blue_coord[0]][n_blue_coord[1]] = "B"
                f(cnt+1, t_board, n_red_coord, n_blue_coord)
        # 좌
        if board[red_coord[0]][red_coord[1]-1] in ".O" or board[blue_coord[0]][blue_coord[1]-1] in ".O":
            red_ball_in_hole, blue_ball_in_hole, n_red_coord, n_blue_coord = tilt(board, red_coord, blue_coord, 2)
            if red_ball_in_hole:
                answer = min(answer, cnt+1)
            elif not blue_ball_in_hole:
                t_board = deepcopy(board)
                t_board[red_coord[0]][red_coord[1]] = "."
                t_board[n_red_coord[0]][n_red_coord[1]] = "R"
                t_board[blue_coord[0]][blue_coord[1]] = "."
                t_board[n_blue_coord[0]][n_blue_coord[1]] = "B"
                f(cnt+1, t_board, n_red_coord, n_blue_coord)
        # 우
        if board[red_coord[0]][red_coord[1]+1] in ".O" or board[blue_coord[0]][blue_coord[1]+1] in ".O":
            red_ball_in_hole, blue_ball_in_hole, n_red_coord, n_blue_coord = tilt(board, red_coord, blue_coord, 3)
            if red_ball_in_hole:
                answer = min(answer, cnt+1)
            elif not blue_ball_in_hole:
                t_board = deepcopy(board)
                t_board[red_coord[0]][red_coord[1]] = "."
                t_board[n_red_coord[0]][n_red_coord[1]] = "R"
                t_board[blue_coord[0]][blue_coord[1]] = "."
                t_board[n_blue_coord[0]][n_blue_coord[1]] = "B"
                f(cnt+1, t_board, n_red_coord, n_blue_coord)

H, W = map(int, stdin.readline().split())
board = [[*i.strip()] for i in stdin]

red_coord, blue_coord, hole_coord = [0, 0], [0, 0], [0, 0]
for row in range(H):
    for col in range(W):
        if board[row][col]=="R":
            red_coord = [row, col]
        elif board[row][col]=="B":
            blue_coord = [row, col]

answer = 11
f(0, board, red_coord, blue_coord)
print(answer if answer<11 else -1)











"""
백준 16935 배열 돌리기 3 (골드5)

* 각 조건에 맞게 하드코딩 구현하면 됨. 배열 인덱스 연습하기 좋음
"""
from sys import stdin

def int_map(): 
    return map(int, stdin.readline().split())

def mirror_up_down():
    global board, H
    for row in range(H//2):
        board[row], board[H-row-1] = board[H-row-1], board[row]

def mirror_left_right():
    global board, H, W
    l, r = W//2, W//2+1 if W%2 else W//2
    for row in range(H):
        board[row][:l], board[row][r:] = board[row][r:][::-1], board[row][:l][::-1]

def rotate_clockwise():
    global board, H, W
    H, W = W, H
    new_board = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            new_board[i][j] = board[W-j-1][i]
    board = new_board

def rotate_counter_clockwise():
    global board, H, W
    H, W = W, H
    new_board = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            new_board[i][j] = board[j][H-i-1]
    board = new_board

def rotate_group_clockwise():
    global board, H, W
    for row in range(H//2):
        board[row][:W//2], board[row][W//2:], board[row+H//2][:W//2], board[row+H//2][W//2:] = \
        board[row+H//2][:W//2], board[row][:W//2], board[row+H//2][W//2:], board[row][W//2:]

def rotate_group_counter_clockwise():
    global board, H, W
    for row in range(H//2):
        board[row][:W//2], board[row][W//2:], board[row+H//2][:W//2], board[row+H//2][W//2:] = \
        board[row][W//2:], board[row+H//2][W//2:], board[row][:W//2], board[row+H//2][:W//2]


H, W, R = int_map()
board = [[*int_map()] for _ in range(H)]
for command in int_map():
    # 상하
    if command==1:
        mirror_up_down()
    # 좌우
    elif command==2:
        mirror_left_right()
    # 시계 rotate
    elif command==3:
        rotate_clockwise()
    # 반시계 rotate
    elif command==4:
        rotate_counter_clockwise()
    # 시계 그룹 rotate
    elif command==5:
        rotate_group_clockwise()
    # 반시계 그룹 rotate
    elif command==6:
        rotate_group_counter_clockwise()
for i in range(H):
    print(*board[i])
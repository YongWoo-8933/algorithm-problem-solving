"""
백준 12100 2048 (골드1)

1. 각 숫자를 이동하고 합치는 move함수 만듦
2. 백트래킹을 통해 모든 4^5가지의 모든 경우의수 탐방
3. 각 경우에서 가장 큰 숫자로 answer 갱신
"""
from sys import stdin, setrecursionlimit
from collections import deque
from copy import deepcopy

setrecursionlimit(10**6)

def f(n: int):
    global answer, board
    if n==5:
        answer = max(answer, max(max(i) for i in board))
    else:
        n += 1
        temp = deepcopy(board)
        for i in range(4):
            move(i)
            f(n)
            board = deepcopy(temp)

def move(direction: int):
    global N, board
    if direction==0 or direction==1:
        # 좌우 방향
        for row in range(N):
            temp = deque()
            additable = True
            if direction==0:
                # 오른쪽으로 정렬
                for col in range(N-1, -1, -1):
                    if board[row][col]:
                        if temp and temp[0]==board[row][col] and additable:
                            temp[0] = 2*board[row][col]
                            additable = False
                        else:
                            temp.appendleft(board[row][col])
                            additable = True
                for col in range(N-1, -1, -1):
                    board[row][col] = temp.pop() if temp else 0
            elif direction==1:
                # 왼쪽으로 정렬
                for col in range(N):
                    if board[row][col]:
                        if temp and temp[-1]==board[row][col] and additable:
                            temp[-1] = 2*board[row][col]
                            additable = False
                        else:
                            temp.append(board[row][col])
                            additable = True
                for col in range(N):
                    board[row][col] = temp.popleft() if temp else 0
    elif direction==2 or direction==3:
        # 상하 방향
        for col in range(N):
            temp = deque()
            additable = True
            if direction==2:
                # 위쪽으로 정렬
                for row in range(N):
                    if board[row][col]:
                        if temp and temp[-1]==board[row][col] and additable:
                            temp[-1] = 2*board[row][col]
                            additable = False
                        else:
                            temp.append(board[row][col])
                            additable = True
                for row in range(N):
                    board[row][col] = temp.popleft() if temp else 0
            elif direction==3:
                # 아래쪽으로 정렬
                for row in range(N-1, -1, -1):
                    if board[row][col]:
                        if temp and temp[0]==board[row][col] and additable:
                            temp[0] = 2*board[row][col]
                            additable = False
                        else:
                            temp.appendleft(board[row][col])
                            additable = True
                for row in range(N-1, -1, -1):
                    board[row][col] = temp.pop() if temp else 0

N = int(stdin.readline())
board = [[*map(int, i.split())] for i in stdin]
answer = 0
f(0)
print(answer)



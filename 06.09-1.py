"""
코드트리 - 고대 문명 유적 탐사
https://www.codetree.ai/training-field/frequent-problems/problems/ancient-ruin-exploration/description?page=1&pageSize=20
"""
from collections import deque
from copy import deepcopy

def rotate(board: list, row: int, col: int) -> list:
    temp1, temp2 = board[row-1][col-1], board[row-1][col]
    board[row-1][col+1], board[row][col+1], temp1, temp2 = temp1, temp2, board[row-1][col+1], board[row][col+1]
    board[row+1][col+1], board[row+1][col], temp1, temp2 = temp1, temp2, board[row+1][col+1], board[row+1][col]
    board[row+1][col-1], board[row][col-1], temp1, temp2 = temp1, temp2, board[row+1][col-1], board[row][col-1]
    board[row-1][col-1], board[row-1][col] = temp1, temp2    
    return board

def rotate_n(board: list, row: int, col: int, n: int) -> list:
    for _ in range(n):
        board = rotate(board, row, col)
    return board

def find(board: list) -> tuple:
    visited = [[0]*5 for _ in range(5)]
    blanks = set()
    while sum(sum(i) for i in visited)<25:
        q = deque()
        history = set()
        for i in range(5):
            for j in range(5):
                if visited[i][j]==0:
                    visited[i][j] = 1
                    q.append((i, j))
                    break
            else:
                continue
            break
        while q:
            row, col = q.popleft()
            history.add((row, col))
            for dx, dy in zip([0, 0, -1, 1], [1, -1, 0, 0]):
                nrow, ncol = row+dy, col+dx
                if 0<=nrow<5 and 0<=ncol<5 and not visited[nrow][ncol] and board[row][col]==board[nrow][ncol]:
                    visited[nrow][ncol] = 1
                    q.append((nrow, ncol))
        if len(history)>2:
            blanks = blanks.union(history)
    for i, j in blanks:
        board[i][j] = 0
    return len(blanks), board

def fill_board(board: list) -> list:
    global pieces
    for col in range(5):
        for row in range(4, -1, -1):
            if board[row][col]==0:
                board[row][col] = pieces.popleft()
    return board

def explore(board: list) -> tuple:
    answer = []
    for row in range(1, 4):
        for col in range(1, 4):
            for rotate_num in range(1, 4):
                temp = deepcopy(board)
                rotated_board = rotate_n(temp, row, col, rotate_num)
                value, blanked_board = find(rotated_board)
                answer.append((value, rotate_num, col, row, blanked_board))
    answer.sort(key=lambda x: (-x[0], x[1], x[2], x[3]))
    if answer[0][0]:
        return answer[0][0], fill_board(answer[0][4])
    else:
        return answer[0][0], answer[0][4]

K, M = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(5)]
pieces = deque(map(int, input().split()))
answer = []
for _ in range(K):
    temp_answer = 0
    # 탐색
    value, board = explore(board)
    # 찾은게 없으면 종료
    if value==0:
        break
    # 찾은게 있으면 추가
    temp_answer += value
    # 2차 순회 시작
    nvalue, nboard = find(board)
    while nvalue:
        temp_answer += nvalue
        nboard = fill_board(nboard)
        nvalue, nboard = find(nboard)
    board = nboard
    answer.append(temp_answer)
print(*answer)










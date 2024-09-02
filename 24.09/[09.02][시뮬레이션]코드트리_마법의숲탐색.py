"""
코드트리 마법의 숲 탐색

1. 골렘의 각 위치에서 아래, 왼쪽, 오른쪽 이동이 가능한지 여부를 함수로 체크
2. 각 골렘에 대해 마지막행까지 이동(아래 > 왼쪽 > 오른쪽 회전 순으로 체크)
3. 이동할 수 없다면 이동 종료. 골렘이 맵 밖으로 빠져나가있다면 MAP clear
4. 골렘이 맵 안에 잘 있다면, MAP에 골렘의 크기만큼 표시하고 exits에 출구 좌표 기록
5. MAP과 exits를 활용해 BFS 시작, 출구좌표일 때만 다른 골렘의 인덱스로 넘어갈 수 있음
6. BFS에서 가장 깊게 들어간 row를 저장하고, 각 iter가 끝날때 answer에 row 합산
"""
from sys import stdin
from collections import deque

# 빈 칸: 0, 골렘: 1~ 
def is_down_possible(row: int, col: int) -> bool:
    global MAP
    if row==-2:
        return MAP[0][col]==0
    else:
        return MAP[row+2][col]==0 and MAP[row+1][col-1]==0 and MAP[row+1][col+1]==0

def is_left_down_possible(row: int, col: int) -> bool:
    global MAP
    if col==1:
        return False
    elif row==-2:
        return MAP[0][col-1]==0
    elif row==-1:
        return MAP[0][col-1]==0 and MAP[0][col-2]==0 and MAP[1][col-1]==0
    elif row==0:
        return MAP[row][col-2]==0 and MAP[row+1][col-2]==0 and MAP[row+1][col-1]==0 and MAP[row+2][col-1]==0
    else:
        return MAP[row-1][col-1]==0 and MAP[row][col-2]==0 and MAP[row+1][col-2]==0 and MAP[row+1][col-1]==0 and MAP[row+2][col-1]==0

def is_right_down_possible(row: int, col: int) -> bool:
    global MAP, W
    if col==W-2:
        return False
    elif row==-2:
        return MAP[0][col+1]==0
    elif row==-1:
        return MAP[0][col+1]==0 and MAP[0][col+2]==0 and MAP[1][col+1]==0
    elif row==0:
        return MAP[row][col+2]==0 and MAP[row+1][col+2]==0 and MAP[row+1][col+1]==0 and MAP[row+2][col+1]==0
    else:
        return MAP[row-1][col+1]==0 and MAP[row][col+2]==0 and MAP[row+1][col+2]==0 and MAP[row+1][col+1]==0 and MAP[row+2][col+1]==0

def add_exit_coord(row: int, col: int, d: int) -> tuple:
    global exits
    exitr, exitc = [(row-1, col), (row, col+1), (row+1, col), (row, col-1)][d]
    exits[exitr][exitc] = True

H, W, K = map(int, stdin.readline().split())
MAP = [[0]*W for _ in range(H)]
exits = [[False]*W for _ in range(H)]
answer = 0
for idx in range(1, K+1):
    col, d = map(int, stdin.readline().split())
    col -= 1
    row = -2
    # 못 움직일 때까지 쭉 내림
    while row<H-2:
        if is_down_possible(row, col):
            row += 1
        elif is_left_down_possible(row, col):
            row += 1
            col -= 1
            d -= 1
            d %= 4
        elif is_right_down_possible(row, col):
            row += 1
            col += 1
            d += 1
            d %= 4
        else:
            break
    # 골렘 몸이 밖에 걸친 경우 -> clear
    if row<1:
        MAP = [[0]*W for _ in range(H)]
        exits = [[False]*W for _ in range(H)]
    # 맵 내에서 멈췄을 경우 -> MAP에 표시하고 BFS 진행
    else:
        MAP[row-1][col] = idx
        MAP[row][col-1:col+2] = [idx]*3
        MAP[row+1][col] = idx
        add_exit_coord(row, col, d)
        q = deque([(idx, row, col)])
        visited = [[False]*W for _ in range(H)]
        deepest_row = 1
        while q:
            i, r, c = q.popleft()
            deepest_row = max(deepest_row, r)
            for newr, newc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0<=newr<H and 0<=newc<W and not visited[newr][newc]:
                    if MAP[newr][newc]==i or (exits[r][c] and MAP[newr][newc]!=0):
                        visited[newr][newc] = True
                        q.append((MAP[newr][newc], newr, newc))
        answer += deepest_row+1
print(answer)
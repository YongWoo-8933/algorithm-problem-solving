"""
백준 15683 감시 (골드3)

1. cctv의 row, col을 기준으로 상/하/좌/우 방향을 바라보는 watch 함수를 만듦
2. watch함수는 현재 방의 상태와 바라보는 방향을 주면 해당 방향의 사각지대를 없애는 함수임
3. 5번 cctv를 찾아 네방향 모두에 대해 watch 실시
4. 재귀를 통해 0행 0열에서 H-1행 W-1열까지 돌리는데,
   해당 칸에 1~4번까지의 cctv가 있다면 모든 방향에 대해 watch를 실시하고
   각각의 결과로 나온 MAP을 다음 재귀값에 전달
5. H-1행 W-1열에 도착하면 사각지대의 갯수를 세고 answer에 갱신
"""
from sys import stdin
from copy import deepcopy

def watch(MAP: list, direction: int, row: int, col: int) -> list:
    global H, W
    new_MAP = deepcopy(MAP)
    # 상
    if direction==0:
        nrow = row-1
        while 0<=nrow and new_MAP[nrow][col]!=6:
            if new_MAP[nrow][col]==0:
                new_MAP[nrow][col]=-1
            nrow -= 1
    # 우
    elif direction==1:
        ncol = col+1
        while ncol<W and new_MAP[row][ncol]!=6:
            if new_MAP[row][ncol]==0:
                new_MAP[row][ncol]=-1
            ncol += 1
    # 하
    elif direction==2:
        nrow = row+1
        while nrow<H and new_MAP[nrow][col]!=6:
            if new_MAP[nrow][col]==0:
                new_MAP[nrow][col]=-1
            nrow += 1
    # 좌
    elif direction==3:
        ncol = col-1
        while 0<=ncol and new_MAP[row][ncol]!=6:
            if new_MAP[row][ncol]==0:
                new_MAP[row][ncol] = -1
            ncol -= 1
    return new_MAP

def f(MAP: list, row: int, col: int):
    global H, W, answer

    if MAP[row][col]==1:
        for i in range(4):
            next_MAP = watch(MAP, i, row, col)
            if row==H-1 and col==W-1:
                answer = min(answer, sum(next_MAP[i].count(0) for i in range(H)))
            elif col==W-1:
                f(next_MAP, row+1, 0)
            else:
                f(next_MAP, row, col+1)
    elif MAP[row][col]==2:
        for i in range(2):
            next_MAP = watch(MAP, i, row, col)
            next_MAP = watch(next_MAP, i+2, row, col)
            if row==H-1 and col==W-1:
                answer = min(answer, sum(next_MAP[i].count(0) for i in range(H)))
            elif col==W-1:
                f(next_MAP, row+1, 0)
            else:
                f(next_MAP, row, col+1)
    elif MAP[row][col]==3:
        for i in range(4):
            next_MAP = watch(MAP, i, row, col)
            next_MAP = watch(next_MAP, (i+1)%4, row, col)
            if row==H-1 and col==W-1:
                answer = min(answer, sum(next_MAP[i].count(0) for i in range(H)))
            elif col==W-1:
                f(next_MAP, row+1, 0)
            else:
                f(next_MAP, row, col+1)
    elif MAP[row][col]==4:
        for i in range(4):
            next_MAP = watch(MAP, i, row, col)
            next_MAP = watch(next_MAP, (i+1)%4, row, col)
            next_MAP = watch(next_MAP, (i+2)%4, row, col)
            if row==H-1 and col==W-1:
                answer = min(answer, sum(next_MAP[i].count(0) for i in range(H)))
            elif col==W-1:
                f(next_MAP, row+1, 0)
            else:
                f(next_MAP, row, col+1)
    else:
        if row==H-1 and col==W-1:
            answer = min(answer, sum(MAP[i].count(0) for i in range(H)))
        elif col==W-1:
            f(MAP, row+1, 0)
        else:
            f(MAP, row, col+1)
    

H, W = map(int, stdin.readline().split())
MAP = [[*map(int, i.split())] for i in stdin]
for row in range(H):
    for col in range(W):
        if MAP[row][col]==5:
            MAP[row][col] = -1
            for i in range(4):
                MAP = watch(MAP, i, row, col)
answer = H*W
f(MAP, 0, 0)
print(answer)
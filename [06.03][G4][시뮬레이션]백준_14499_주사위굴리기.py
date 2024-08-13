"""
백준 14499 주사위 굴리기

1. roll 함수로 주사위의 각면 값들 update
2. 각 조건에 맞게 보드/주사위값 update
3. 주사위 상단값 print
"""
from sys import stdin

H, W, row, col, _ = map(int, stdin.readline().split())
MAP = [[*map(int, stdin.readline().split())] for _ in range(H)]
commands = [*map(int, stdin.readline().split())]
#       전 후 좌 우 상 하
dice = [0, 0, 0, 0, 0, 0]

# 주사위를 굴리는 함수 
# 보드와 상관없이 주사위 모양만 바꿈
def roll(dice: list, direction: int) -> list:
    if direction==1:
        # 우이동: 상->우, 우->하, 하->좌, 좌->상
        return [dice[0], dice[1], dice[5], dice[4], dice[2], dice[3]]
    elif direction==2:
        # 좌이동: 상->좌, 좌->하, 하->우, 우->상
        return [dice[0], dice[1], dice[4], dice[5], dice[3], dice[2]]
    elif direction==3:
        # 후이동: 상->후, 후->하, 하->전, 전->상
        return [dice[5], dice[4], dice[2], dice[3], dice[0], dice[1]]
    elif direction==4:
        # 전이동: 상->전, 후->상, 하->후, 전->하
        return [dice[4], dice[5], dice[2], dice[3], dice[1], dice[0]]
    
#     마진      우      좌        후      전
d = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
for command in commands:
    d_row, d_col = d[command]
    if 0<=row+d_row<H and 0<=col+d_col<W:
        row += d_row
        col += d_col
        dice = roll(dice, command)
        if MAP[row][col]==0:
            # 칸이 0이면 주사위 바닥값 칸에 복사
            MAP[row][col] = dice[5]
        else:
            # 칸이 0이 아니면 칸값 주사위 바닥면으로 복사후 칸값 0으로
            dice[5] = MAP[row][col]
            MAP[row][col] = 0
        print(dice[4])
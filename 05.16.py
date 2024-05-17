"""
백준 17144 미세먼지 안녕!

※ 주의할점: 모든 실행을 전역 환경에서 하면 파이썬에서는 시간초과로 안풀림.
            함수를 만들어서 모듈화 하면 시간 단축효과가 있어 풀리는듯..

1. 하드코딩 구현
"""
from sys import stdin

def diffuse(origin_map):
    new_map = [[0]*W for _ in range(H)]
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for row in range(H):
        for col in range(W):
            dust = origin_map[row][col]
            new_dust = int(dust/5)
            count = 0
            if new_dust:
                for dx, dy in d:
                    new_row, new_col = row+dy, col+dx
                    if 0<=new_row<H and 0<=new_col<W and origin_map[new_row][new_col]!=-1:
                        new_map[new_row][new_col] += new_dust
                        count += 1
            new_map[row][col] += dust-new_dust*count
    return new_map

def top_cycle(origin_map, top_ac_row, W):
    temp = origin_map[top_ac_row][1]
    origin_map[top_ac_row][1] = 0
    for col in range(2, W):
        origin_map[top_ac_row][col], temp = temp, origin_map[top_ac_row][col]
    for row in range(top_ac_row-1, -1, -1):
        origin_map[row][W-1], temp = temp, origin_map[row][W-1]
    for col in range(W-2, -1, -1):
        origin_map[0][col], temp = temp, origin_map[0][col]
    for row in range(1, top_ac_row):
        origin_map[row][0], temp = temp, origin_map[row][0]
    return origin_map

def bottom_cycle(origin_map, bot_ac_row, H):
    temp = origin_map[bot_ac_row][1]
    origin_map[bot_ac_row][1] = 0
    for col in range(2, W):
        origin_map[bot_ac_row][col], temp = temp, origin_map[bot_ac_row][col]
    for row in range(bot_ac_row+1, H):
        origin_map[row][W-1], temp = temp, origin_map[row][W-1]
    for col in range(W-2, -1, -1):
        origin_map[H-1][col], temp = temp, origin_map[H-1][col]
    for row in range(H-2, bot_ac_row, -1):
        origin_map[row][0], temp = temp, origin_map[row][0]
    return origin_map

H, W, T = map(int, stdin.readline().split())
MAP = [[*map(int, i.split())] for i in stdin]
top_ac_row, bot_ac_row = [i for i in range(H) if MAP[i][0] == -1]

for _ in range(T):
    MAP = diffuse(MAP)
    MAP = top_cycle(MAP, top_ac_row, W)
    MAP = bottom_cycle(MAP, bot_ac_row, H)

print(sum(sum(MAP[i]) for i in range(H))+2)

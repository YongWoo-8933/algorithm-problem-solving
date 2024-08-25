"""
백준 17143 낚시왕 (골드1)

1. 낚시왕이 각 열을 움직이며 가까운 상어를 죽이고, 상어가 이동하는 것을 추적하면 된다.
2. 현재 상어들의 위치를 표시하는 MAP 리스트와 상어들의 상태를 저장하는 sharks 리스트
   두 가지를 모두 활용해야 시간초과가 안남
3. 상어들의 방향/속력값에따라 다음 상어의 위치가 어디일지 계산하는게 복잡하므로
   이부분을 구현하고 디버깅하는게 관건임
"""
from sys import stdin

H, W, M = map(int, stdin.readline().split())
sharks = []
for i in stdin:
    r, c, s, d, z = map(int, i.split())
    sharks.append([True, r, c, s, d, z])
MAP = [[-1]*(W+1) for _ in range(H+1)]
for idx, (live, r, c, s, d, z) in enumerate(sharks):
    MAP[r][c] = idx
answer = 0

# 가장 가까운 상어 죽이기
def kill_shark(col: int):
    global MAP, sharks, answer, H 
    for row in range(1, H+1):
        shark_idx = MAP[row][col]
        if shark_idx>=0:
            sharks[shark_idx][0] = False
            answer += sharks[shark_idx][5]
            MAP[row][col] = -1
            break

# 상어들 이동
def move_sharks():
    global MAP, sharks, H, W, M
    visited = {}
    for idx in range(M):
        live, r, c, s, d, z = sharks[idx]
        if MAP[r][c]==idx:
            MAP[r][c] = -1
        if live:
            # 속력만큼 이동
            if d in [1, 2]:
                s %= 2*H-2
            elif d in [3, 4]:
                s %= 2*W-2
            if d==1:
                if s<r:
                    r -= s
                elif r<=s<r+H-1:
                    d = 2
                    r = s-r+2
                else:
                    r += 2*H-2-s
            elif d==2:
                if s<H-r+1:
                    r += s
                elif H-r+1<=s<2*H-r:
                    d = 1
                    r = 2*H-s-r
                else:
                    r -= 2*H-2-s
            elif d==3:
                if s<W-c+1:
                    c += s
                elif W-c+1<=s<2*W-c:
                    d = 4
                    c = 2*W-s-c
                else:
                    c -= 2*W-2-s
            elif d==4:
                if s<c:
                    c -= s
                elif c<=s<c+W-1:
                    d = 3
                    c = s-c+2
                else:
                    c += 2*W-2-s

            # 이동 마친 칸에 상어 있는 경우
            if (r, c) in visited:
                # 칸에 있던 상어보다 현재 상어가 더 큰 경우 -> 칸 상어 죽이고 MAP 갱신
                if sharks[visited[(r, c)]][5]<z:
                    sharks[visited[(r, c)]][0] = False
                    visited[(r, c)] = idx
                    MAP[r][c] = idx
                    sharks[idx][1], sharks[idx][2], sharks[idx][4] = r, c, d
                # 칸에 있던 상어가 더 큰 경우 -> 현재 상어 죽이기
                else:
                    sharks[idx][0] = False

            # 이동 마친 칸에 상어가 없는 경우
            else:
                visited[(r, c)] = idx
                MAP[r][c] = idx
                sharks[idx][1], sharks[idx][2], sharks[idx][4] = r, c, d

for king_col in range(1, W+1):
    kill_shark(king_col)
    move_sharks()

print(answer)











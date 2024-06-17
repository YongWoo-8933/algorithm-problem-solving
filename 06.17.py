"""
백준 17143 낚시왕

문제
낚시왕이 상어 낚시를 하는 곳은 크기가 R×C인 격자판으로 나타낼 수 있다. 
격자판의 각 칸은 (r, c)로 나타낼 수 있다. r은 행, c는 열이고, 
(R, C)는 아래 그림에서 가장 오른쪽 아래에 있는 칸이다. 칸에는 상어가 최대 한 마리 들어있을 수 있다. 
상어는 크기와 속도를 가지고 있다.



낚시왕은 처음에 1번 열의 한 칸 왼쪽에 있다. 다음은 1초 동안 일어나는 일이며, 아래 적힌 순서대로 일어난다. 
낚시왕은 가장 오른쪽 열의 오른쪽 칸에 이동하면 이동을 멈춘다.

낚시왕이 오른쪽으로 한 칸 이동한다.
낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
상어가 이동한다.
상어는 입력으로 주어진 속도로 이동하고, 속도의 단위는 칸/초이다. 
상어가 이동하려고 하는 칸이 격자판의 경계를 넘는 경우에는 방향을 반대로 바꿔서 속력을 유지한채로 이동한다.

왼쪽 그림의 상태에서 1초가 지나면 오른쪽 상태가 된다. 
상어가 보고 있는 방향이 속도의 방향, 왼쪽 아래에 적힌 정수는 속력이다. 왼쪽 위에 상어를 구분하기 위해 문자를 적었다.


상어가 이동을 마친 후에 한 칸에 상어가 두 마리 이상 있을 수 있다. 
이때는 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다.

낚시왕이 상어 낚시를 하는 격자판의 상태가 주어졌을 때, 낚시왕이 잡은 상어 크기의 합을 구해보자.

입력
첫째 줄에 격자판의 크기 R, C와 상어의 수 M이 주어진다. (2 ≤ R, C ≤ 100, 0 ≤ M ≤ R×C)

둘째 줄부터 M개의 줄에 상어의 정보가 주어진다. 
상어의 정보는 다섯 정수 r, c, s, d, z (1 ≤ r ≤ R, 1 ≤ c ≤ C, 0 ≤ s ≤ 1000, 1 ≤ d ≤ 4, 1 ≤ z ≤ 10000) 로 
이루어져 있다. (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기이다. 
d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다.

두 상어가 같은 크기를 갖는 경우는 없고, 하나의 칸에 둘 이상의 상어가 있는 경우는 없다.
출력
낚시왕이 잡은 상어 크기의 합을 출력한다.

예제 입력 1 
4 6 8
4 1 3 3 8
1 3 5 2 9
2 4 8 4 1
4 5 0 1 4
3 3 1 2 7
1 5 8 4 3
3 6 2 1 2
2 2 2 3 5
예제 출력 1 
22

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
                    r = s-r+1
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
                    c = s-c+1
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











"""
승자독식 모노폴리
https://www.codetree.ai/training-field/frequent-problems/problems/odd-monopoly/description?page=2&pageSize=20
"""
from sys import stdin

n, m, k = map(int, stdin.readline().split())
# [점유플레이어, 남은 k]
board = [[[0, 0] for __ in range(n)] for _ in range(n)]
players = [[] for _ in range(m+1)]
# 보드 점유 상태와 플레이어의 초기 위치 저장
for i in range(n):
    temp = [*map(int, stdin.readline().split())]
    for j in range(n):
        if temp[j]!=0:
            board[i][j] = [temp[j], k]
            players[temp[j]] = [True, 0, i, j]
# 플레이어의 초기 방향 저장
for i, d in enumerate(map(int, stdin.readline().split())):
    players[i+1][1] = d
# 플레이어의 방향우선순위 저장
priorities = [[[] for _ in range(5)] for _ in range(m+1)]
for i in range(1, m+1):
    for j in range(1, 5):
        priorities[i][j] = [*map(int, stdin.readline().split())]

for i in range(1000):
    # 플레이어 1 생존 여부 체크
    if not players[1][0]:
        print(-1)
        exit()

    # 나머지 플레이어 존재 여부 체크
    for exist, _, _, _ in players[2:]:
        if exist:
            break
    else:
        print(i)
        exit()

    # 이동
    for player_idx in range(1, m+1):
        player_exist, player_d, player_row, player_col = players[player_idx]
        if not player_exist:
            continue
        # 점유되지 않은 칸, 자신이 점유한 칸 검토
        not_occupancied = []
        self_occupancied = []
        for dx, dy in zip([0, 0, -1, 1], [1, -1, 0, 0]):
            nrow, ncol =  player_row+dy, player_col+dx
            if 0<=nrow<n and 0<=ncol<n:
                if dy==1:
                    if board[nrow][ncol][0]==0:
                        not_occupancied.append((2, nrow, ncol))
                    elif board[nrow][ncol][0]==player_idx:
                        self_occupancied.append((2, nrow, ncol))
                elif dy==-1:
                    if board[nrow][ncol][0]==0:
                        not_occupancied.append((1, nrow, ncol))
                    elif board[nrow][ncol][0]==player_idx:
                        self_occupancied.append((1, nrow, ncol))
                elif dx==1:
                    if board[nrow][ncol][0]==0:
                        not_occupancied.append((4, nrow, ncol))
                    elif board[nrow][ncol][0]==player_idx:
                        self_occupancied.append((4, nrow, ncol))
                elif dx==-1:
                    if board[nrow][ncol][0]==0:
                        not_occupancied.append((3, nrow, ncol))
                    elif board[nrow][ncol][0]==player_idx:
                        self_occupancied.append((3, nrow, ncol))
        # 점유되지 않은 칸 존재
        if not_occupancied:
            for pd in priorities[player_idx][player_d]:
                for nd, nrow, ncol in not_occupancied:
                    if pd==nd:
                        players[player_idx] = [True, nd, nrow, ncol]
                        break
                else:
                    continue
                break
        # 점유되지 않은 칸 없음 -> # 자신이 점유한 칸 검토
        else:
            for pd in priorities[player_idx][player_d]:
                for nd, nrow, ncol in self_occupancied:
                    if pd==nd:
                        players[player_idx] = [True, nd, nrow, ncol]
                        break
                else:
                    continue
                break

    # board 갱신 -> k값 1씩감소
    #            -> 겹치는 유저 체크
    for row in range(n):
        for col in range(n):
            current_players = []
            for player_idx in range(1, m+1):
                player_exist, _, player_row, player_col = players[player_idx]
                if player_exist and row==player_row and col==player_col:
                    current_players.append(player_idx)
            # 해당 칸에 플레이어 존재
            if current_players:
                current_players.sort()
                # 가장 작은 index의 플레이어로 선정 
                board[row][col] = [current_players[0], k]
                # 나머지 플레이어 소멸
                if len(current_players)>1:
                    for idx in current_players[1:]:
                        players[idx][0] = False
            # 해당칸에 플레이어 없음
            else:
                # k값이 0이 아닐 경우 1 줄이기
                if board[row][col][1]:
                    board[row][col][1] -= 1
                # k값이 0이 됐다면 점유 플레이어 없애기
                if board[row][col][1]==0:
                    board[row][col][0] = 0

print(-1)
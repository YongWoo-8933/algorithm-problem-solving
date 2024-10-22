"""
백준 19237 어른상어 (골드1)

1. dp로 진행. dp[i]에는 i번째 날짜 이후 얻을 수 있는 최대 금액을 저장
2. 뒤에서부터 거꾸로 dp 테이블 제작 -> 현재 상담을 넣었을때 vs 넣지 않았을때 비교
"""

from sys import stdin

N, M, k = map(int, stdin.readline().split())
# 상어 존재여부, 상어 방향, 냄새 주인, 냄새 남은시간
MAP = [[[False, 0, 0, 0] for __ in range(N)] for _ in range(N)]
for row in range(N):
    lst = [*map(int, stdin.readline().split())]
    for col in range(N):
        if lst[col]!=0:
            MAP[row][col] = [True, 0, lst[col], k]
directions = [0] + [*map(int, stdin.readline().split())]
for row in range(N):
    for col in range(N):
        if MAP[row][col]:
            MAP[row][col][1] = directions[MAP[row][col][2]]
# 1: 상, 2: 하, 3: 좌, 4: 우
direction_priorities = [[]]
for _ in range(M):
    temp = [[]]
    for __ in range(4):
        temp.append([*map(int, stdin.readline().split())])
    direction_priorities.append(temp)

d = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
sec = 0
while sec<=1000:
    sec += 1
    new_MAP = [[[False, 0, 0, 0] for __ in range(N)] for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if MAP[row][col][0]:
                cur_shark_idx = MAP[row][col][2]
                no_smell_nodes = []
                my_smell_nodes = []
                for i in range(1, 5):
                    dy, dx = d[i]
                    nrow, ncol = row+dy, col+dx
                    if 0<=nrow<N and 0<=ncol<N:
                        if MAP[nrow][ncol][2]==0:
                            no_smell_nodes.append((i, nrow, ncol))
                        elif MAP[nrow][ncol][2]==cur_shark_idx:
                            my_smell_nodes.append((i, nrow, ncol))
                cur_shark_direction = MAP[row][col][1]
                if len(no_smell_nodes)>1:
                    for prefer_direction in direction_priorities[cur_shark_idx][cur_shark_direction]:
                        for new_direction, nrow, ncol in no_smell_nodes:
                            if prefer_direction==new_direction:
                                new_node_occupied = new_MAP[nrow][ncol][0]
                                new_node_shark_idx = new_MAP[nrow][ncol][2]
                                if not new_node_occupied or (new_node_occupied and cur_shark_idx<new_node_shark_idx):
                                    new_MAP[nrow][ncol] = [True, new_direction, cur_shark_idx, k]
                                break
                        else:
                            continue
                        break
                elif len(no_smell_nodes)==1:
                    new_direction, nrow, ncol = no_smell_nodes.pop()
                    new_node_occupied = new_MAP[nrow][ncol][0]
                    new_node_shark_idx = new_MAP[nrow][ncol][2]
                    if not new_node_occupied or (new_node_occupied and cur_shark_idx<new_node_shark_idx):
                        new_MAP[nrow][ncol] = [True, new_direction, cur_shark_idx, k]
                elif len(my_smell_nodes)>1:
                    for prefer_direction in direction_priorities[cur_shark_idx][cur_shark_direction]:
                        for new_direction, nrow, ncol in my_smell_nodes:
                            if prefer_direction==new_direction:
                                new_node_occupied = new_MAP[nrow][ncol][0]
                                new_node_shark_idx = new_MAP[nrow][ncol][2]
                                if not new_node_occupied or (new_node_occupied and cur_shark_idx<new_node_shark_idx):
                                    new_MAP[nrow][ncol] = [True, new_direction, cur_shark_idx, k]
                                break
                        else:
                            continue
                        break
                elif len(my_smell_nodes)==1:
                    new_direction, nrow, ncol = my_smell_nodes.pop()
                    new_node_occupied = new_MAP[nrow][ncol][0]
                    new_node_shark_idx = new_MAP[nrow][ncol][2]
                    if not new_node_occupied or (new_node_occupied and cur_shark_idx<new_node_shark_idx):
                        new_MAP[nrow][ncol] = [True, new_direction, cur_shark_idx, k]
                MAP[row][col][0] = False
    cnt = 0
    for row in range(N):
        for col in range(N):
            if not new_MAP[row][col][0] and MAP[row][col][3]>1:
                new_MAP[row][col] = [False, 0, MAP[row][col][2], MAP[row][col][3]-1]
            elif new_MAP[row][col][0]:
                cnt += 1
    if cnt==1:
        print(sec)
        exit()
    MAP = new_MAP
print(-1)

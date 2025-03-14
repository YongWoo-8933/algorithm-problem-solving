"""
백준 19237 어른상어 (골드1)

** 빡센 시뮬레이션, 별다른 아이디어없이 구현만 하면 됨 **
"""

from sys import stdin


def main():
    N, M, k = map(int, stdin.readline().split())


    # 상어 존재여부, 상어 방향, 냄새 주인, 냄새 남은시간
    MAP = [[[False, 0, 0, 0] for __ in range(N)] for _ in range(N)]
    for row in range(N):
        lst = [*map(int, stdin.readline().split())]
        for col in range(N):
            if lst[col]!=0:
                MAP[row][col] = [True, 0, lst[col], k]
    # [[False, 0, 0, 0], [False, 0, 0, 0], [False, 0, 0, 0]]
    # [[False, 0, 0, 0], [True , 0, 1, 4], [False, 0, 0, 0]]
    # [[False, 0, 0, 0], [False, 0, 0, 0], [False, 0, 0, 0]]
    # [[True , 0, 2, 4], [False, 0, 0, 0], [False, 0, 0, 0]]


    directions = [0] + [*map(int, stdin.readline().split())]
    for row in range(N):
        for col in range(N):
            if MAP[row][col]:
                MAP[row][col][1] = directions[MAP[row][col][2]]
    # [[False, 0, 0, 0], [False, 0, 0, 0], [False, 0, 0, 0]]
    # [[False, 0, 0, 0], [True , 1, 1, 4], [False, 0, 0, 0]]
    # [[False, 0, 0, 0], [False, 0, 0, 0], [False, 0, 0, 0]]
    # [[True , 3, 2, 4], [False, 0, 0, 0], [False, 0, 0, 0]]


    # 1: 상, 2: 하, 3: 좌, 4: 우
    direction_priorities = [[]]
    for _ in range(M):
        temp = [[]]
        for __ in range(4):
            temp.append([*map(int, stdin.readline().split())])
        direction_priorities.append(temp)
    # [
    #   [],  <- 0번은 비워놓음
    #   [[1, 2, 0, 3], [2, 1, 3, 0], [0, 1, 3, 2], [1, 3, 4, 2]],  <- 1번 상어의 방향별 선호
    #   [[0, 1, 3, 2], [1, 3, 4, 2], [1, 2, 0, 3], [2, 1, 3, 0]],  <- 2번 상어의 방향별 선호
    # ]


    d = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
    sec = 0
    while sec<=1000:
        cnt = 0  # 상어가 맵에 몇마리 남았는지 체크 => 1마리면 종료
        new_MAP = [[[False, 0, 0, 0] for __ in range(N)] for _ in range(N)]
        for row in range(N):
            for col in range(N):
                if MAP[row][col][0]:
                    cnt += 1
                    cur_shark_idx = MAP[row][col][2]  # 현재칸 상어의 번호
                    no_smell_nodes = []   # 현재칸 주변에 냄새가 없는 노드를 저장
                    my_smell_nodes = []   # 현재칸 주변에 자신의 냄새가 있는 노드를 저장
                    for i in range(1, 5):
                        dy, dx = d[i]
                        nrow, ncol = row+dy, col+dx
                        if 0<=nrow<N and 0<=ncol<N:
                            if MAP[nrow][ncol][2]==0:
                                # 노드의 (방향, 행, 열) 추가
                                no_smell_nodes.append((i, nrow, ncol))
                            elif MAP[nrow][ncol][2]==cur_shark_idx:
                                my_smell_nodes.append((i, nrow, ncol))
                    cur_shark_direction = MAP[row][col][1]  # 현재칸 상어의 방향


                    # 현재칸 주변에 냄새가 없는 노드가 여러개임 > 선호 방향 순으로 찾아 이동
                    if len(no_smell_nodes)>1:
                        for prefer_direction in direction_priorities[cur_shark_idx][cur_shark_direction]:
                            for new_direction, nrow, ncol in no_smell_nodes:
                                if prefer_direction==new_direction:
                                    new_node_occupied = new_MAP[nrow][ncol][0]
                                    new_node_shark_idx = new_MAP[nrow][ncol][2]
                                    # 해당칸에 이미 상어가 있다면, 번호를 비교해 작은 경우에만 강탈
                                    if not new_node_occupied or (new_node_occupied and cur_shark_idx<new_node_shark_idx):
                                        new_MAP[nrow][ncol] = [True, new_direction, cur_shark_idx, k]
                                    break
                            else:
                                continue
                            break

                    # 현재칸 주변에 냄새가 없는 노드가 한개임 > 해당 방향으로 이동
                    elif len(no_smell_nodes)==1:
                        new_direction, nrow, ncol = no_smell_nodes.pop()
                        new_node_occupied = new_MAP[nrow][ncol][0]
                        new_node_shark_idx = new_MAP[nrow][ncol][2]
                        if not new_node_occupied or (new_node_occupied and cur_shark_idx<new_node_shark_idx):
                            new_MAP[nrow][ncol] = [True, new_direction, cur_shark_idx, k]

                    # 현재칸 주변에 자신의 냄새가 있는 칸이 여러개임 > 선호 방향 순으로 이동
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
                    
                    # 현재칸 주변에 자신의 냄새가 있는 칸이 한개임 > 해당 방향으로 이동
                    elif len(my_smell_nodes)==1:
                        new_direction, nrow, ncol = my_smell_nodes.pop()
                        new_node_occupied = new_MAP[nrow][ncol][0]
                        new_node_shark_idx = new_MAP[nrow][ncol][2]
                        if not new_node_occupied or (new_node_occupied and cur_shark_idx<new_node_shark_idx):
                            new_MAP[nrow][ncol] = [True, new_direction, cur_shark_idx, k]
                    MAP[row][col][0] = False

        # 맵에 상어가 한마리면 종료
        if cnt==1:
            print(sec)
            exit()
        
        # 맵에 상어가 여러마리면 시간 추가
        sec += 1

        # 칸을 순회하며 냄새의 유효시간 1초씩 줄이기
        # new_MAP 생성 당시 모든 칸들이 초기화 되어있기때문에,
        # 1초 이상 냄새가 남은 칸에 대해서만 진행하면됨
        for row in range(N):
            for col in range(N):
                if not new_MAP[row][col][0] and MAP[row][col][3]>1:
                    new_MAP[row][col] = [False, 0, MAP[row][col][2], MAP[row][col][3]-1]
        MAP = new_MAP
    print(-1)
main()
"""
백준 17142 연구소 3 (골드3)

1. 조건에 맞게 BFS 시뮬레이션 돌리면 됨
2. 초기 활성 바이러스의 위치를 combinations로 특정함
3. ** 비활성 바이러스가 활성 바이러스와 만나면 활성화 된다는게 포인트
4. 3번에 주의해서 비활성화된 바이러스가 있는 칸으로 이동 시에는 answer를 갱신하지 않았음
5. 결국 빈칸에 바이러스가 확산될때만 카운트되며 적절한 답을 낼 수 있게됨
"""
from sys import stdin
from itertools import combinations
from copy import deepcopy
from collections import deque

N, M = map(int, stdin.readline().split())
MAP = []
virus_coords = []
for row in range(N):
    lst = [*map(int, stdin.readline().split())]
    for col in range(N):
        if lst[col]==2:
            virus_coords.append((row, col))
    MAP.append(lst)
answer = None
for activated_virus_comb in combinations(virus_coords, M):
    temp_map = deepcopy(MAP)
    temp_answer = 0
    q = deque()
    for row, col in activated_virus_comb:
        q.append((0, row, col))
        temp_map[row][col] = 3
    while q:
        cnt, row, col = q.popleft()
        for nrow, ncol in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
            if 0<=nrow<N and 0<=ncol<N:
                if temp_map[nrow][ncol] in {0, 2}:
                    if temp_map[nrow][ncol]==0:
                        temp_answer = max(temp_answer, cnt+1)
                    temp_map[nrow][ncol] = 3
                    q.append((cnt+1, nrow, ncol))
    for row in range(N):
        if 0 in temp_map[row]:
            break
    else:
        if answer is None:
            answer = temp_answer
        else:
            answer = min(answer, temp_answer)
print(-1 if answer is None else answer)
"""
백준 16236 아기 상어 (골드3)

1. 시작 지점(9) 부터 BFS시작
2. 먹을 수 있는 물고기를 만나면 eatable_fish 리스트에 좌표와 거리 추가
3-1. BFS 종료후 먹을 수 있는 물고기가 없으면 종료
3-2. 먹을 수 있는 물고기가 있다면, 물고기중 가장 가까운>위의>왼쪽의 물고기 선정
4. 해당 물고기를 먹고 + 먹은자리 비우기 + BFS 시작좌표 갱신 + 총소요시간 갱신
5. 상어가 먹은 물고기수 체크 > 사이즈만큼 먹으면 사이즈업
"""
from sys import stdin
from collections import deque

N = int(stdin.readline())
MAP = [[*map(int, i.split())] for i in stdin]
start_row, start_col = [(i, j) for i in range(N) for j in range(N) if MAP[i][j]==9][0]
MAP[start_row][start_col] = 0
total_time, current_size, eat_fish_num = 0, 2, 0
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while 1:
    q = deque([(0, start_row, start_col)])
    check = [[1]*N for _ in range(N)]
    check[start_row][start_col] = 0
    eatable_fish = []
    while q:
        time, row, col = q.popleft()
        if 0 < MAP[row][col] < current_size:
            eatable_fish.append((row, col, time))
            continue
        time += 1
        for dx, dy in d:
            next_row, next_col = row+dy, col+dx
            if 0<=next_row<N and 0<=next_col<N and check[next_row][next_col] and MAP[next_row][next_col]<=current_size:
                check[next_row][next_col] = 0
                q.append((time, next_row, next_col))
    if eatable_fish:
        min_row, min_col, min_time = eatable_fish[0]
        for i, j, t in eatable_fish[1:]:
            if t < min_time or (t == min_time and (i<min_row or (i==min_row and j<min_col))):
                min_row, min_col, min_time = i, j, t
        MAP[min_row][min_col] = 0
        total_time += min_time
        start_row, start_col = min_row, min_col
        eat_fish_num += 1
        if eat_fish_num == current_size:
            current_size += 1
            eat_fish_num = 0
    else:
        break
print(total_time)

    


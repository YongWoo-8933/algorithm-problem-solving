"""
백준 2573 빙산 (골드4)

1. while문을 통해 순회 시작
2. 각 순회에서 BFS를 하는데, 맨처음 시작점을 찾기 위해 빙산이 남아있는
   좌표를 찾아냄. 없을 경우 0을 리턴하고 프로그램 종료
3. 빙산 시작점을 찾았다면 BFS시작. 각 좌표에서 녹을 양을 계산하고,
   인접한 빙산이 있다면 q에 추가
4. BFS가 종료된 후 BFS를 위해 방문체크했던 visited array를
   BFS시작 전 MAP상태와 비교해 빙산의 이분 여부를 조사
5. 이분됐을 경우 day를 출력하고 프로그램 종료, 아닐 경우 다음 순회 진행
"""
from sys import stdin
from collections import deque

def f(MAP: list, H: int, W: int, day: int) -> list:
    q = deque()
    new_MAP = [[0]*W for _ in range(H)]
    visited = [[0]*W for _ in range(H)]
    for row in range(H):
        for col in range(W):
            if MAP[row][col]!=0:
                q.append((row, col))
                visited[row][col] = 1
                break
        else:
            continue
        break
    else:
        print(0)
        exit()
    while q:
        row, col = q.popleft()
        zero_cnt = 0
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nrow, ncol = row+dy, col+dx
            if 0<=nrow<H and 0<=ncol<W:
                if MAP[nrow][ncol]==0:
                    zero_cnt += 1
                elif not visited[nrow][ncol]:
                    visited[nrow][ncol] = 1
                    q.append((nrow, ncol))
        new_MAP[row][col] = MAP[row][col]-min(MAP[row][col], zero_cnt)
    for row in range(H):
        for col in range(W):
            if MAP[row][col] and not visited[row][col]:
                print(day)
                exit()
    return new_MAP

H, W = map(int, stdin.readline().split())
MAP = [[*map(int, i.split())] for i in stdin]
day = 0
while 1:
    MAP = f(MAP, H, W, day)
    day += 1
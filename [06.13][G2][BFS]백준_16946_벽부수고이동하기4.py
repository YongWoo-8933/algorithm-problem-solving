"""
백준 16946 벽 부수고 이동하기 4 (골드2)

1. H행 W열만큼의 answer arr 생성, i행 j열에 있는 벽을 없앴을때 칸의 수를 의미
2. 벽이 아닌(0인) 좌표에서 BFS 시작
3. 각 BFS에서 이동한 칸의 수를 카운트하고(cnt) 만난 벽의 좌표를 기억해놓음(walls)
4. 해당 BFS가 끝나면, 만났던 벽 좌표들을 순회하며 cnt만큼 answer arr에 추가해줌
"""
from sys import stdin
from collections import deque
from copy import deepcopy

H, W = map(int, stdin.readline().split())
board = [[*map(int, i.strip())] for i in stdin]
visited = deepcopy(board)
answer = deepcopy(board)

for srow in range(H):
    for scol in range(W):
        if not visited[srow][scol]:
            visited[srow][scol] = 1
            q = deque([(srow, scol)])
            walls = set()
            cnt = 0
            while q:
                row, col = q.popleft()
                cnt += 1
                for dx, dy in zip([0, 0, -1, 1], [1, -1, 0, 0]):
                    nrow, ncol = row+dy, col+dx
                    if 0<=nrow<H and 0<=ncol<W:
                        if board[nrow][ncol]:
                            walls.add((nrow, ncol))
                        elif not visited[nrow][ncol]:
                            visited[nrow][ncol] = 1
                            q.append((nrow, ncol))
            for row, col in walls:
                answer[row][col] += cnt
                answer[row][col] %= 10

for i in range(H):
    print("".join(map(str, answer[i])))





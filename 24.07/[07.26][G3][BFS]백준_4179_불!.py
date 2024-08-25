"""
백준 4179 불! (골드3)

1. BFS로 불과 지훈이가 동시에 움직이며, 불이 먼저 움직이게 하면됨
2. BFS는 최소 이동을 보장하므로, 불을 먼저 / 지훈이를 나중에 q에 추가하면
   이후 활동은 알아서 보장됨. 지훈이를 마킹하기 위해 cnt를 2씩 추가
3. j_num 변수를 운영해 만약 q에 지훈이의 이동경우가 하나도 없다면 그대로 종료
"""
from sys import stdin
from collections import deque

H, W = map(int, stdin.readline().split())
MAP = [i.strip() for i in stdin]
q = deque()
f_visited = [[False]*W for _ in range(H)]
j_visited = [[False]*W for _ in range(H)]
jrow, jcol = 0, 0
for row in range(H):
    for col in range(W):
        if MAP[row][col]=="J":
            jrow, jcol = row, col
        elif MAP[row][col]=="F":
            q.append((1, row, col))
            f_visited[row][col] = True
q.append((2, jrow, jcol))
j_visited[jrow][jcol] = True
j_num = 1
while q:
    cnt, row, col = q.popleft()
    # 불
    if cnt%2:
        for nrow, ncol in [(row+1, col), (row-1, col), (row, col-1), (row, col+1)]:
            if 0<=nrow<H and 0<=ncol<W and MAP[nrow][ncol]!="#" and not f_visited[nrow][ncol]:
                f_visited[nrow][ncol] = True
                q.append((cnt+2, nrow, ncol))
    # 지훈
    else:
        j_num -= 1
        if row==H-1 or row==0 or col==W-1 or col==0:
            print(cnt//2)
            exit()
        for nrow, ncol in [(row+1, col), (row-1, col), (row, col-1), (row, col+1)]:
            if 0<=nrow<H and 0<=ncol<W and MAP[nrow][ncol]!="#" and not j_visited[nrow][ncol] and not f_visited[nrow][ncol]:
                j_visited[nrow][ncol] = True
                j_num += 1
                q.append((cnt+2, nrow, ncol))
        if not j_num:
            break
print("IMPOSSIBLE")
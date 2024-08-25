"""
softeer 나무 섭지

1. 출구 좌표 찾아 저장
2. 출구에서부터 남우와 유령에게 각각 BFS 시작
3. 남우에게 닿았는지 여부 + 몇 칸 걸렸는지 저장
4. 유령에게 닿았는지 여부 + 몇 칸 걸렸는지 저장
5. 남우에게 닿지 못했다면 -> 탈출 실패
   남우에게 닿고 유령에게 닿지 못했다면 -> 탈출 성공
   남우에게 닿고 유령에게도 닿았으며 남우가 출구까지 더 가깝다면 -> 탈출 성공
   그 외 경우 -> 탈출 실패
"""
from sys import stdin
from collections import deque

H, W = map(int, stdin.readline().split())
board = [i.strip() for i in stdin]
for exit_row in range(H):
    for exit_col in range(W):
        if board[exit_row][exit_col]=="D":
            break
    else:
        continue
    break

q = deque([(0, exit_row, exit_col)])
visited = [[0]*W for _ in range(H)]
visited[exit_row][exit_col] = 1
N_escape = False
while q:
    N_cnt, row, col = q.popleft()
    if board[row][col]=="N":
        N_escape = True
        break
    N_cnt += 1
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nrow, ncol = row+dy, col+dx
        if 0<=nrow<H and 0<=ncol<W and not visited[nrow][ncol] and board[nrow][ncol]!="#":
            visited[nrow][ncol] = 1
            q.append((N_cnt, nrow, ncol))

q = deque([(0, exit_row, exit_col)])
visited = [[0]*W for _ in range(H)]
visited[exit_row][exit_col] = 1
G_exist = False
while q:
    G_cnt, row, col = q.popleft()
    if board[row][col]=="G":
        G_exist = True
        break
    G_cnt += 1
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nrow, ncol = row+dy, col+dx
        if 0<=nrow<H and 0<=ncol<W and not visited[nrow][ncol]:
            visited[nrow][ncol] = 1
            q.append((G_cnt, nrow, ncol))

if not N_escape:
    print("No")
elif not G_exist:
    print("Yes")
elif N_cnt<G_cnt:
    print("Yes")
else:
    print("No")
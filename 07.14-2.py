"""
백준 2589 보물섬 (골드5)

1. 막다른 길인 칸을 찾아냄(이어진 길이 1개 뿐인 칸)
2. 한개뿐인 칸이 없다면 2개뿐인 칸을 찾아냄
3. 해당 칸을 시점으로 BFS를 돌리고, 가장 멀리 뻗어나간 경우를 찾아 answer에 갱신
"""
from sys import stdin
from collections import deque

H, W = map(int, stdin.readline().split())
MAP = [i.strip() for i in stdin]
starts_1, starts_2 = [], []
for r in range(H):
    for c in range(W):
        if MAP[r][c]=="L":
            cnt = 0
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r+dy, c+dx
                if 0<=nr<H and 0<=nc<W and MAP[nr][nc]=="L":
                    cnt += 1
            if cnt==1:
                starts_1.append((r, c))
            elif cnt==2:
                starts_2.append((r, c))
answer = 0
starts = starts_1 if starts_1 else starts_2
while starts:
    srow, scol = starts.pop()
    q = deque([(0, srow, scol)])
    visited = [[0]*W for _ in range(H)]
    visited[srow][scol] = 1
    while q:
        cnt, row, col = q.popleft()
        answer = max(answer, cnt)
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nrow, ncol = row+dy, col+dx
            if 0<=nrow<H and 0<=ncol<W and MAP[nrow][ncol]=="L" and not visited[nrow][ncol]:
                visited[nrow][ncol] = 1
                q.append((cnt+1, nrow, ncol))
print(answer)
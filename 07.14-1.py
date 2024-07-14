"""
백준 1261 알고스팟 (골드4)

1. 평범한 BFS에서, visited(방문여부)를 만들 때 해당 칸까지 부숴야 하는 벽의 수를 저장하기로 함
2. 다음 칸으로 이동하기 전 visited에 저장된 갯수보다 더 많이 벽을 부숴야 하는지 체크
3. 벽을 적게 부순 경우가 먼저 탐색되도록 heap을 사용
"""
from sys import stdin
from heapq import heappush, heappop

W, H = map(int, stdin.readline().split())
MAP = [i.strip() for i in stdin]
visited = [[W*H]*W for _ in range(H)]
visited[0][0] = 0
q = []
heappush(q, (0, 0, 0))
while q:
    cnt, row, col = heappop(q)
    if row==H-1 and col==W-1:
        print(cnt)
        break
    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nrow, ncol = row+dy, col+dx
        if 0<=nrow<H and 0<=ncol<W:
            ncnt = cnt if MAP[nrow][ncol]=="0" else cnt+1
            if ncnt<visited[nrow][ncol]:
                visited[nrow][ncol] = ncnt
                heappush(q, (ncnt, nrow, ncol))
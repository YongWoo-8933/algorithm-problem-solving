"""
백준 2146 다리 만들기 (골드3)

1. DFS로 각 섬들에 고유한 넘버 마킹(BFS했다가 자꾸 메모리 초과나서 DFS로 바꿈)
2. N*N의 모든 지점에 대해 해당 지점이 해안가라면, BFS 진행
3. BFS는 바다를 타고 진행되며 자신이 출발한 섬의 고유 넘버와 다른 섬을 만나면 종료
**4. visited table을 운영해 방문했던 노드를 체크하는데, 단순히 bool 여부를 체크하는게 아니라
     바다의 해당 지점까지 최소 다리 길이로 갱신함
     ex) 3행 5열지점까지 오면서 만든 다리의 길이가 2라면, 2로 저장
         이후 시행에서 3행 5열지점까지 오면서 다리의 길이가 2보다 크거나 같으면
         더이상 다리를 이을 필요가 없으므로 종료
"""
from sys import stdin, setrecursionlimit
from collections import deque

def marking_dfs(land_num: int, row: int, col: int):
    global MAP, d
    MAP[row][col] = land_num
    for dy, dx in d:
        nrow, ncol = row+dy, col+dx
        if 0<=nrow<N and 0<=ncol<N and MAP[nrow][ncol]==1:
            marking_dfs(land_num, nrow, ncol)

N = int(stdin.readline())
setrecursionlimit(10**6)
MAP = [[*map(int, i.split())] for i in stdin]
d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
cur_land_num = 2
for r in range(N):
    for c in range(N):
        if MAP[r][c]==1:
            marking_dfs(cur_land_num, r, c)
            cur_land_num += 1

answer = 200
visited = [[200]*N for _ in range(N)]
for srow in range(N):
    for scol in range(N):
        if MAP[srow][scol]==0:
            continue

        q = deque()
        for dy, dx in d:
            nrow, ncol = srow+dy, scol+dx
            if 0<=nrow<N and 0<=ncol<N and MAP[nrow][ncol]==0:
                q.append((0, srow, scol))
                visited[srow][scol] = 0
                break
        if not q: 
            continue

        land_num = MAP[srow][scol]
        find_land = False
        while q and not find_land:
            cnt, row, col = q.popleft()
            if cnt>=answer:
                break
            for dy, dx in d:
                nrow, ncol = row+dy, col+dx
                if 0<=nrow<N and 0<=ncol<N:
                    x = MAP[nrow][ncol]
                    if x>1 and x!=land_num:
                        answer = min(answer, cnt)
                        find_land = True
                        break
                    elif x==0 and cnt+1<visited[nrow][ncol]:
                        visited[nrow][ncol] = cnt+1
                        q.append((cnt+1, nrow, ncol))
print(answer)
        
    


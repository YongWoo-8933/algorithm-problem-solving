"""
백준 3055 탈출 (골드4)

1. 고슴도치가 이동하기 전에 반드시 물이 먼저 확산되어야 한다는게 포인트
2. 이를 실행하기 위해 BFS를 진행할 때 물과 고슴도치 사이에 우선순위 설정
3. day를 2씩 증가시켰으며, 물은 홀수/고슴도치는 짝수 day를 설정함
4. 이후 이 day값을 튜플의 가장 앞에있는 값으로 두고, 
   BFS를 돌릴때 heapq를 사용해 day가 가장 작은 row/col조합부터
   수행하도록 제한함
5. 고슴도치가 굴로 무사히 도착하면 day//2값을 리턴,
   도착하지 못한다면 문자열 출력
"""
from sys import stdin
from heapq import heappop, heappush

H, W = map(int, stdin.readline().split())
MAP = [[*i] for i in stdin]
hq = []
visited = [[0]*W for _ in range(H)]
for row in range(H):
    for col in range(W):
        if MAP[row][col]=="*":
            heappush(hq, (1, row, col))
        elif MAP[row][col]=="S":
            MAP[row][col] = "."
            heappush(hq, (2, row, col))
while hq:
    day, row, col = heappop(hq)
    new_day = day+2
    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nrow, ncol = row+dy, col+dx
        if day%2:
            # 물인 경우
            if 0<=nrow<H and 0<=ncol<W and MAP[nrow][ncol]==".":
                MAP[nrow][ncol] = "*"
                heappush(hq, (new_day, nrow, ncol))
        else:
            # 고슴도치인 경우
            if 0<=nrow<H and 0<=ncol<W and not visited[nrow][ncol]:
                if MAP[nrow][ncol]=="D":
                    print(day//2)
                    exit()
                elif MAP[nrow][ncol]==".":
                    visited[nrow][ncol] = 1
                    heappush(hq, (new_day, nrow, ncol))
print("KAKTUS")
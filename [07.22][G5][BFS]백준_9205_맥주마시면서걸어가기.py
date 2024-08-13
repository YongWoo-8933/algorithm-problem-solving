"""
백준 9205 맥주 마시면서 걸어가기 (골드5)

** 두 좌표 사이의 거리가 맨해튼거리임을 유의
1. hq를 생성하고 (목적지까지의 거리, 행, 열)의 튜플 저장
2. 처음에는 출발지점의 정보를 넣고
3. 해당 점에서 갈수있는 편의점(거리가 1000이내인 모든 편의점)들을 찾아
   hq에 (거리, 행, 열) 튜플로 추가
4. 목적지에 도달하면 happy 출력 후 다음 테케,
   목적지에 도달하지 못하고 hq가 비어버리면 sad 출력 후 다음 테케
"""
from sys import stdin
from heapq import heappop, heappush

input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    srow, scol = map(int, input().split())
    stores = [[*map(int, input().split())] for _ in range(n)]
    erow, ecol = map(int, input().split())
    hq = []
    heappush(hq, (abs(erow-srow)+abs(ecol-scol), srow, scol))
    visited = {(srow, scol)}
    while hq:
        _, row, col = heappop(hq)
        if abs(erow-row)+abs(ecol-col)<=1000:
            print("happy")
            break
        for store_row, store_col in stores:
            if (store_row, store_col) not in visited and abs(store_row-row)+abs(store_col-col)<=1000:
                visited.add((store_row, store_col))
                heappush(hq, (abs(erow-store_row)+abs(ecol-store_col), store_row, store_col))
    else:
        print("sad")
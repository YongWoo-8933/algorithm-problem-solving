"""
백준 1277 발전소 설치 (골드 4)

1. 다익스트라 태그 힌트 받고 품
2. 각 좌표를 저장해놓고, 연결된 발전소 정보 저장
3. 1에서부터 시작해 모든 발전소로의 이동정보를 hq에 추가
4. heapq로 구현함으로써 항상 가장 적은 비용을 가지는 이동이 먼저 실행되도록함
5. visited를 저장할 때 각 노드로 이동하는 최소비용을 저장해 시행횟수 제한
"""
from sys import stdin
from heapq import heappop, heappush

N, W = map(int, stdin.readline().split())
M = float(stdin.readline())
coords = [[0, 0]] + [[*map(int, stdin.readline().split())] for _ in range(N)]
links = [set() for _ in range(N+1)]
for i in stdin:
    fr, to = map(int, i.split())
    links[fr].add(to)
    links[to].add(fr)
hq = [(0, 1)]
visited = [float("inf")]*(N+1)
visited[1] = 0
while hq:
    cnt, node = heappop(hq)
    if node==N:
        print(int(cnt*1000)) 
        break
    x, y = coords[node]
    for next_node in links[node]:
        if cnt<visited[next_node]:
            visited[next_node] = cnt
            heappush(hq, (cnt, next_node))
    for next_node in range(1, N+1):
        nx, ny = coords[next_node]
        l = ((nx-x)**2+(ny-y)**2)**0.5
        if l<=M and cnt+l<visited[next_node]:
            visited[next_node] = cnt+l
            heappush(hq, (cnt+l, next_node))
    
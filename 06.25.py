"""
백준 13334 철로 (골드2)

1. 각 사람의 집, 사무실 좌표를 **대소관계에 유의하여** 받음
2. 각 사람의 집/사무실 중 오른쪽 좌표 기준 정렬
3. heap을 구현하고, 각 오른쪽 좌표를 철로의 오른쪽 끝으로 했을때 철로에 들어오는 경우
   heap을 유지, 들어오지 않는 모든 좌표를 pop해냄
4. 각 순회마다 힙에 들어있는 좌표의 수를 answer에 갱신
"""
from sys import stdin
from heapq import heappush, heappop

N = int(stdin.readline())
lst = []
for _ in range(N):
    a, b = map(int, stdin.readline().split())
    lst.append((min(a, b), max(a, b)))
D = int(stdin.readline())
lst.sort(key=lambda x: x[1])

q = []
answer = 0
for h, o in lst:
    heappush(q, h)
    while q and q[0]<o-D:
        heappop(q)
    answer = max(answer, len(q))

print(answer)

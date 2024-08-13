"""
백준 2887 행성 터널

1. 각 행성들을 축별로 분해하는게 키포인트임
2. 분해된 각 축의 좌표를 기반으로 간선의 거리를 정렬하고
3. 크루스칼 알고리즘을 통해 최소 스패닝 트리를 구함
"""

from sys import stdin
from heapq import heappop, heappush

def find(x: int) -> int:
    global parents
    if parents[x]!=x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a: int, b: int):
    global parents
    ra, rb = find(a), find(b)
    if ra!=rb:
        parents[max(ra, rb)] = min(ra, rb)

N = int(input())
planet_x, planet_y, planet_z = [], [], []
for i in range(N):
    x, y, z = map(int, stdin.readline().split())
    planet_x.append((x, i))
    planet_y.append((y, i))
    planet_z.append((z, i))
planet_x.sort()
planet_y.sort()
planet_z.sort()

q = []
for i in range(N-1):
    for values in [planet_x, planet_y, planet_z]:
        v1, i1 = values[i]
        v2, i2 = values[i+1]
        heappush(q, (v2-v1, i1, i2))

parents = [*range(N)]
answer = 0
while q:
    dist, idx1, idx2 = heappop(q)
    if find(idx1)!=find(idx2):
        answer += dist
        union(idx1, idx2)

print(answer)





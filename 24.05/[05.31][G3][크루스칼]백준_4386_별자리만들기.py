"""
백준 4386 별자리 만들기 (골드3)

1. 점의 갯수가 100개이고, 모든 점이 모든 나머지 점에대해 가중치의 간선을 가지는 그래프라고 생각할 수 있음
2. 최대 100C2 개의 간선에 대해 kruskal 알고리즘 진행
"""
from sys import stdin

def find(parents: list, x: int) -> int:
   if parents[x] != x:
      parents[x] = find(parents, parents[x])
   return parents[x]

def union(parents: list, a: int, b: int) -> list:
   parent_a, parent_b = find(parents, a), find(parents, b)
   if parent_a != parent_b:
      parents[max(parent_a, parent_b)] = min(parent_a, parent_b)
   return parents

N = int(stdin.readline())
coords = [[*map(float, i.split())] for i in stdin]
lst = []
for i in range(N):
   x1, y1 = coords[i]
   for j in range(N):
      if i!=j:
         x2, y2 = coords[j]
         lst.append((((x1-x2)**2+(y1-y2)**2)**0.5, i, j))
lst.sort(key=lambda x: -x[0])
parents = [i for i in range(N)]
answer, count = 0, 0
while count<N-1:
   dist, node1, node2 = lst.pop()
   if find(parents, node1)!=find(parents, node2):
      union(parents, node1, node2)
      answer += dist
      count += 1
print(answer)








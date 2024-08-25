"""
백준 1197 최소 스패닝 트리 (골드4)

* 프림 / 크루스칼 알고리즘 두가지 풀이 진행
- 프림 알고리즘: 한 노드에서 시작해 연결된 노드를 탐색함.
  (BFS와 유사)  이 때 weight가 작은 경로부터 탐색(우선순위 큐를 통해 구현)
                방문한 노드를 체크하며 모든 노드를 방문했다면 자동으로 종료.
- 크루스칼 알고리즘: 모든 간선을 가중치 오름차순으로 정렬 후,
                    유니온 파인드 알고리즘을 통해 사이클이 생기지 않도록
                    간선을 추가하며 MST를 찾아냄.
==> 백준 실행결과 prim대비 kruskal이 실행시간, 메모리 측면에서 훨씬 빠름
"""
from sys import stdin
from heapq import heappop, heappush
V, E = map(int, stdin.readline().split())

# 1. prim 알고리즘
links = [set() for _ in range(V+1)]
for i in stdin:
    fr, to, weight = map(int, i.split())
    links[fr].add((to, weight))
    links[to].add((fr, weight))
q = [(0, 1)]
visited = set()
answer = 0
while q:
    weight, node = heappop(q)
    if node not in visited:
        visited.add(node)
        answer += weight
        for next_node, next_weight in links[node]:
            heappush(q, (next_weight, next_node))
print(answer)

# 2. kruskal 알고리즘
links = [[*map(int, i.split())] for i in stdin]
links.sort(key=lambda x: x[2])
roots = [i for i in range(V+1)]

def find(roots: list, x: int) -> int:
    nx = roots[x]
    if nx != x:
        roots[x] = find(roots, nx)
    return roots[x]

def union(roots: list, a: int, b: int) -> list:
    root_a, root_b = find(roots, a), find(roots, b)
    roots[max(root_a, root_b)] = min(root_a, root_b)
    return roots

answer = 0
for A, B, weight in links:
    if find(roots, A) != find(roots, B):
        answer += weight
        roots = union(roots, A, B)
print(answer)


    


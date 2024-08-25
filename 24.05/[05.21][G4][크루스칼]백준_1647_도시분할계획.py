"""
백준 1647 도시분할계획 (골드4)

1. 크루스칼 알고리즘을 기반으로 함
2. 최소 스패닝 트리를 구할 때, 가중치가 가장 큰 '마지막 간선을 추가하지 않는다'면
   최소한의 비용으로 노드들을 두 집합으로 구분할 수 있게됨
3. 따라서 크루스칼 알고리즘을 통해 구한 유지비 합에서 마지막에 더했던 cost값을 뺀값을 출력
"""
from sys import stdin
N, M = map(int, stdin.readline().split())
roads = [[*map(int, i.split())] for i in stdin]
roads.sort(key=lambda x: x[2])
roots = [i for i in range(N+1)]

def find(roots: list, x: int) -> int:
    if roots[x]!=x:
        roots[x] = find(roots, roots[x])
    return roots[x]

def union(roots: list, a: int, b: int) -> list:
    root_a, root_b = find(roots, a), find(roots, b)
    roots[max(root_b, root_a)] = min(root_b, root_a)
    return roots

answer = 0
last_cost = 0
for a, b, cost in roads:
    if find(roots, a) != find(roots, b):
        roots = union(roots, a, b)
        answer += cost
        last_cost = cost
print(answer-last_cost)

        


    


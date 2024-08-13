"""
백준 23324 어려운 모든 정점 쌍 최단 거리

1. union-find 구현
2. 가중치가 1인 간선을 제외하고, 나머지 간선의 양 끝 노드에 대해 union 실행
3. 2를 완료했을 때 집합이 1개면 모든 정점간 거리는 0
4. 집합이 2개면 각 집합의 원소수를 곱한게 정답 
"""
from sys import stdin

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

N, M, K = map(int, stdin.readline().split())
parents = [i for i in range(N+1)]
for idx, value in enumerate(stdin):
    a, b = map(int, value.split())
    if idx+1!=K:
        union(a, b)

result = {}
for i in range(1, N+1):
    x = find(i)
    if x in result:
        result[x] += 1
    else:
        result[x] = 1

if len(result)==1:
    answer = 0
else:
    answer = 1
    for i in result.values():
        answer *= i

print(answer)



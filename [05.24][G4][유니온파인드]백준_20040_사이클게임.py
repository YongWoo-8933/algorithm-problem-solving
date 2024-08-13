"""
백준 20040 사이클 게임 (골드4)

1. 사이클 발생 여부를 따져야하므로, union-find 알고리즘 활용
2. 전형적인 union-find 알고리즘 구현 후, 사이클이 발견되면 종료하고 몇번째인지 출력
"""
from sys import stdin

def find(parents: list, x: int) -> int:
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]

def union(parents: list, a: int, b: int) -> list:
    parent_a, parent_b = find(parents, a), find(parents, b)
    if parent_a != parent_b:
        parents[max(parent_a, parent_b)] = parents[min(parent_a, parent_b)]
    return parents

N, M = map(int, stdin.readline().split())
answer = 0
parents = [i for i in range(N)]
for turn in range(1, M+1):
    a, b = map(int, stdin.readline().split())
    if find(parents, a) != find(parents, b):
        union(parents, a, b)
    else:
        answer = turn
        break
print(answer)


    


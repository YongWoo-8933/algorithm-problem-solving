"""
백준 15681 트리와 쿼리 (골드5)

1. 각 노드를 루트로 하는 서브트리의 갯수를 의미하는 배열 answer 생성
2. dfs를 돌며 재귀를 통해 각 노드의 하위 노드갯수를 갱신 
"""
from sys import stdin, setrecursionlimit

def dfs(node: int):
    global tree, answer
    answer[node] = 1
    for next_node in tree[node]:
        if answer[next_node]==0:
            dfs(next_node)
            answer[node] += answer[next_node]

setrecursionlimit(10**6)
N, R, Q = map(int, stdin.readline().split())
tree = [set() for _ in range(N+1)]
for _ in range(N-1):
    fr, to = map(int, stdin.readline().split())
    tree[fr].add(to)
    tree[to].add(fr)

answer = [0]*(N+1)
dfs(R)

for i in stdin:
    print(answer[int(i)])



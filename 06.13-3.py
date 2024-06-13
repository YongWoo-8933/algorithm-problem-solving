"""
백준 10775 공항

1. gi값이 주어지면 해당 G가 비어있는지 확인하고, 빈 게이트를 찾을때까지 이전 게이트를 찾아야함
2. root를 찾아간다는 개념에서, union-find의 활용가능성을 찾는게 관건
3. 주어진 gi값의 root를 find함수로 찾고, root가 0보다 크면(비어있는 게이트가 있으면) root-1과 root를 union함
4. gi root값이 0이라는건 gate 1번까지 모두 찼다는 뜻이므로 break
5. count한 answer를 return
"""
from sys import stdin

def find(parents: list, node: int) -> int:
    if node!=parents[node]:
        parents[node] = find(parents, parents[node])
    return parents[node]

def union(parents: list, a: int, b: int) -> list:
    root_a, root_b = find(parents, a), find(parents, b)
    if root_a!=root_b:
        parents[max(root_a, root_b)] = min(root_a, root_b)
    return parents

G = int(stdin.readline())
P = int(stdin.readline())
answer = 0
parents = [i for i in range(G+1)]
lst = [int(i) for i in stdin]
for i in lst:
    root = find(parents, i)
    if root > 0:
        union(parents, root-1, root)
        answer += 1
    else:
        break
print(answer)









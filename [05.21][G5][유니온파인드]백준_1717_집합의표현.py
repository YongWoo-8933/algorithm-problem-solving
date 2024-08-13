"""
백준 1717 집합의 표현 (골드5)

1. 유니온 파인드 알고리즘 진행
2. find 함수에서 경로압축 반드시 할 것
"""
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
N, T = map(int, stdin.readline().split())
roots = [i for i in range(N+1)]

def find(roots: list, x: int) -> int:
    nx = roots[x]
    if nx != x:
        roots[x] = find(roots, nx)
    return roots[x]

def union(roots: list, a: int, b: int) -> list:
    root_a, root_b = find(roots, a), find(roots, b)
    roots[max(root_a, root_b)] = min(root_a, root_b)
    return roots

for _ in range(T):
    option, A, B = map(int, stdin.readline().split())
    if option:
        print("YNEOS"[find(roots, A)!=find(roots, B)::2])
    else:
        roots = union(roots, A, B)

    


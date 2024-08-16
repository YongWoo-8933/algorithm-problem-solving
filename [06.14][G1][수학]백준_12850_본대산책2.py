"""
백준 12850 본대 산책2 (골드1)

1. a 노드에서 b 노드까지 D번의 과정을 거쳐 가는 경우의 수는
   -> 해당 그래프의 인접행렬 G를 작성한 후 G를 D제곱한 행렬의 a -> b 값을 구하면 된다.
2. 아이디어만 이해하고 있으면 간단한 행렬의 분할제곱 문제가 됨
"""
from math import log2
from copy import deepcopy

def multiply(A: list, B: list) -> list:
    X = [[0]*8 for _ in range(8)]
    for row in range(8):
        for col in range(8):
            X[row][col] = sum(A[row][k]*B[k][col] for k in range(8))%1000000007
    return X

D = int(input())
G = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]
]
n_lst = []
while D:
    x = int(log2(D))
    n_lst.append(x)
    D -= 2**x

answer = [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1]
]
for n in n_lst:
    X = deepcopy(G)
    for _ in range(n):
        X = multiply(X, X)
    answer = multiply(answer, X)

print(answer[0][0])











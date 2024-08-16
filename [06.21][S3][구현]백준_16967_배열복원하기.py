"""
백준 16967 배열 복원하기 (실버3)

1. 배열의 특징을 파악하고 복원
"""
from sys import stdin

H, W, X, Y = map(int, stdin.readline().split())
B = [[*map(int, i.split())] for i in stdin]
A = [[0]*W for _ in range(H)]
for row in range(H):
    print(row)
for row in range(H):
    for col in range(W):
        A[row][col] = B[row][col]
for row in range(X, H+X):
    for col in range(Y, W+Y):
        if 0<=row<H and 0<=col<W:
            A[row][col] -= A[row-X][col-Y]
for i in range(H):
    print(*A[i])



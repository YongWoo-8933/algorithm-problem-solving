"""
백준 9555 대회 장소 준비

1. 박수합을 dp table에 계산
2. K개 열의 박수합중 큰값 산출
"""
from sys import stdin

input = stdin.readline
H, W = map(int, input().split())
MAP = [[*map(int, input().split())] for _ in range(H)]
K = int(input())

dp = [[0]*(W+1) for _ in range(H+1)]
for i in range(H):
    for j in range(W):
        dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + MAP[i][j]

answer = 0
for col in range(K, W+1):
    answer = max(answer, dp[-1][col]-dp[-1][col-K])

print(answer)






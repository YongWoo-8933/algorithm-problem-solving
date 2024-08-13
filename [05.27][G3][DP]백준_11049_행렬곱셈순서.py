"""
백준 11049 행렬 곱셈 순서

1. dp풀이 - 복잡해서 해답 참고함
"""
from sys import stdin
N = int(stdin.readline())
lst = []
for i in stdin:
    a, b = map(int, i.split())
    lst.append((a, b))
dp = [[0]*(N) for _ in range(N)]
for i in range(N-1):
    dp[i][i+1] = lst[i][0] * lst[i+1][0] * lst[i+1][1]
for i in range(N-2, 0, -1):
    for j in range(i):
        row, col = j, N-i+j
        dp[row][col] = float("inf")
        for k in range(N-i):
            dp[row][col] = min(dp[row][col], dp[row][row+k] + dp[row+k+1][col] + lst[row][0]*lst[row+k][1]*lst[col][1])
print(dp[0][N-1])




"""
백준 10942 팰린드롬? (골드4)

1. dp 활용
2. dp테이블은 N x N 크기로, 수열 S의 row번째 수에서 col번째 수가 팰린드롬인지 정보를 저장  
3. row == col이면 당연히 1
4. row+1 == col이면 S[row] == S[col]일경우 1, 아니면 0
5. 나머지 row, col에 대해, S[row] == S[col]일경우 dp[row+1][col-1]이 1이면 1, 그 외 경우 0 
"""
from sys import stdin

N = int(stdin.readline())
sequence = [*map(int, stdin.readline().split())]
dp = [[0]*N for _ in range(N)]
for i in range(N):
    dp[i][i] = 1
for i in range(N-1):
    dp[i][i+1] = [0, 1][sequence[i]==sequence[i+1]]
for i in range(2, N):
    for j in range(N-i):
        row, col = j, j+i
        dp[row][col] = [0, dp[row+1][col-1]][sequence[row]==sequence[col]]
stdin.readline()
for i in stdin:
    s, e = map(int, i.split())
    print(dp[s-1][e-1])


    


"""
백준 2758 로또 (골드4)

1. 전형적인 dp문제로, m개중 n개를 뽑는 경우를 dp[n][m]에 저장해나감
2. dp[n][m] = m을 뽑지 않고 m-1개중 n개를 뽑는 경우 + m을 미리 뽑고 m//2개 중 n개를 뽑는 경우 
3. 따라서 dp[n][m] = dp[i][j] = dp[i][j-1] + dp[i-1][j//2] 임을 활용해 dp 테이블 작성
4. n, m을 받아 출력
"""
from sys import stdin

def main():
    dp = [[0]*(2001) for _ in range(11)]
    dp[0] = [1]*2001
    for i in range(1, 11):
        for j in range(1, 2001):
            dp[i][j] = dp[i][j-1] + dp[i-1][j//2]
    for _ in range(int(stdin.readline())):
        n, m = map(int, stdin.readline().split())
        print(dp[n][m])

main()
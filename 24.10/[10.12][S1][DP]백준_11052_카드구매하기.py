"""
백준 11052 카드 구매하기 (실버1)

1. 처음부터 dp로 쭉 돌리면 됨..
"""

def main():
    N = int(input())
    prices = [0]+[*map(int, input().split())]
    dp = [0]*(N+1)
    dp[1] = prices[1]
    for i in range(N+1):
        dp[i] = prices[i]
        for j in range(i//2+1):
            dp[i] = max(dp[i], dp[j]+dp[i-j])
    print(dp[N])
main()
"""
백준 2225 합분해 (골드 5)

1. 원리는 모르겠지만, dp table의 행열을 N, K로 두고 운영
2. 한행전 + 한열전 값이 해당 값이됨.
"""
def main():
    N, K = map(int, input().split())
    dp = [1]*(K+1)
    for _ in range(1, N+1):
        new_dp = [0]
        for i in range(1, K+1):
            new_dp.append((new_dp[-1]+dp[i])%1000000000)
        dp = new_dp
    print(dp[K])
main()
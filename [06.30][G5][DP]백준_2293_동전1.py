"""
백준 2293 동전1 (골드 5)
* 고민해도 잘 모르겠어서 해답 찾아봄
https://mong9data.tistory.com/68
"""
from sys import stdin

_, K = map(int, stdin.readline().split())
dp = [0]*(K+1)
dp[0] = 1
coins = [int(i) for i in stdin if int(i)<=K]
for coin in coins:
    for i in range(coin, K+1):
        dp[i] += dp[i-coin]
print(dp[K])


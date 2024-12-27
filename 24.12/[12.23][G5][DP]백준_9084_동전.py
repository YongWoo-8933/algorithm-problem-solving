"""
백준 9084 동전 (골드5)

1. dp로 금액별 경우의 수를 쌓아가며 계산
"""
from sys import stdin

def main():
    for _ in range(int(stdin.readline())):
        stdin.readline()
        coins = [*map(int, stdin.readline().split())]
        M = int(stdin.readline())
        dp = [0]*(M+1)
        dp[0] = 1
        for coin in coins:
            for m in range(M+1):
                if dp[m]!=0 and m+coin<=M:
                    dp[m+coin] += dp[m]
        print(dp[-1])

main()
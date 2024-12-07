"""
백준 11048 이동하기 (실버2)

1. dp로 왼쪽칸에서 오는 경우와 위쪽칸에서 오는 경우중 더 많이 먹는 경우를 택하면됨
"""
from sys import stdin

def main():
    H, W = map(int, stdin.readline().split())
    MAP = [[*map(int, i.split())] for i in stdin]
    dp = [0]*(W+1)
    for row in range(H):
        for col in range(W):
            dp[col+1] = max(dp[col], dp[col+1])+MAP[row][col]
    print(dp[W])

main()

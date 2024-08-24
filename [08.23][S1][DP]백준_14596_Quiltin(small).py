"""
백준 14596 Quilting (Small) (실버 1)

1. 평범한 DP문제로, 모든 칸에 대해 각 칸이 선택됐을 때 가질 수 있는
   최소값을 DP table에 저장해나감.
"""
from sys import stdin

def main():
    H, W = map(int, stdin.readline().split())
    B1 = [[*map(int, stdin.readline().split())] for _ in range(H)]
    B2 = [[*map(int, i.split())] for i in stdin]
    dp = [0]*W
    INF = (255**2)*10
    for row in range(H):
        new_dp = [0]*W
        for col in range(W):
            min_value = INF
            for c in [col-1, col, col+1]:
                if 0<=c<W:
                    min_value = min(min_value, dp[c])
            new_dp[col] = min_value+(B1[row][col]-B2[row][col])**2
        dp = new_dp
    print(min(dp))

main()
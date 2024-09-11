"""
백준 28450 컨벤 데드가 하고싶어요 (실버2)

1. 평범한 dp 파이프 잇기 문제
2. 왼쪽 위에서부터 가장 적은 눈치력으로 올 수 있는 경우만 dp table에 저장
"""
from sys import stdin

def main():
    H, W = map(int, stdin.readline().split())
    gym = [[*map(int, stdin.readline().split())] for _ in range(H)]
    dp = [[float("inf")]*(W+1) for _ in range(H+1)]
    dp[0][1] = 0
    for row in range(1, H+1):
        for col in range(1, W+1):
            dp[row][col] = gym[row-1][col-1]+min(dp[row-1][col], dp[row][col-1])
    if dp[H][W]>int(stdin.readline()):
        print("NO")
    else:
        print("YES", dp[H][W])
        
main()
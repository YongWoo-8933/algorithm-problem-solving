"""
백준 1915 가장 큰 정사각형 (골드 4)

1. 배열합 dp table 제작
2. 길이 1부터 정사각형이 존재하는지 찾아가며 최대 정사각형 넓이 산출
"""
from sys import stdin

def main():
    H, W = map(int, stdin.readline().split())
    board = [i.strip() for i in stdin]
    dp = [[0]*(W+1) for _ in range(H+1)]
    for row in range(H):
        for col in range(W):
            dp[row+1][col+1] = dp[row][col+1]+dp[row+1][col]-dp[row][col]+[0, 1][board[row][col]=="1"]
    for length in range(1, min(H, W)+1):
        for row in range(H-length+1):
            for col in range(W-length+1):
                area = dp[row+length][col+length]
                area -= dp[row+length][col]
                area -= dp[row][col+length]
                area += dp[row][col]
                if area==length**2:
                    break
            else:
                continue
            break
        else:
            print((length-1)**2)
            exit()
    print(length**2)
main()
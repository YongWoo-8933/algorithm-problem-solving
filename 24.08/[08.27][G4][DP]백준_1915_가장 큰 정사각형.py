"""
백준 1915 가장 큰 정사각형 (골드 4)

[내 풀이]
1. 배열합 dp table 제작
2. 이분탐색으로 길이 1부터 정사각형이 존재하는지 찾아가며 최대 정사각형 넓이 산출

[정답 확인]
1. 각 행에대해 dp table 제작 후
2. dp table의 열 값에 현재까지 발견된 가장 큰 정사각형의 넓이를 저장
"""
from sys import stdin

# 내 풀이
def is_exist(dp: list, length: int) -> bool:
    for row in range(len(dp)-length):
        for col in range(len(dp[0])-length):
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
        return False
    return True

def main():
    H, W = map(int, stdin.readline().split())
    board = [i.strip() for i in stdin]
    dp = [[0]*(W+1) for _ in range(H+1)]
    for row in range(H):
        for col in range(W):
            dp[row+1][col+1] = dp[row][col+1]+dp[row+1][col]-dp[row][col]+[0, 1][board[row][col]=="1"]
    l, r = 1, min(H, W)+1
    while l<=r:
        c = (l+r)//2
        if is_exist(dp, c):
            l = c+1
        else:
            r = c-1
    print(r**2)
main()

# 정답 풀이
def main():
    H, W = map(int, stdin.readline().split())
    board = [i.strip() for i in stdin]
    dp = [0]*W
    answer = 0
    for row in range(H):
        new_dp = [0]*W
        new_dp[0] = 1 if board[row][0]=="1" else 0
        for col in range(1, W):
            if board[row][col]=="1":
                new_dp[col] = min(dp[col-1], dp[col], new_dp[col-1])+1
        answer = max(answer, max(new_dp))
        dp = new_dp
    print(answer**2)
main()
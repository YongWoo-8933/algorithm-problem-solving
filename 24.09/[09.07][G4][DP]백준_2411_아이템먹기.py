"""
백준 2411 아이템 먹기 (골드4)

1. 맵 크기만큼의 dp table을 운영해야함.
2. 각 칸에는 2개의 값이 저장되는데, 해당 칸까지 오는 경로의 수 / 오면서 먹은 아이템의 수다.
3. for 문을 돌며 dp table을 갱신할 때, 왼쪽에서 오는 경우 + 아래에서 오는 경우를 구하면 된다.
4. 다만 여기서 해당 칸까지 오며 먹은 아이템의 수가 많은쪽을 저장하고, 같을 경우 합한다.
5. 마지막 칸의 경로 수를 반환하되, 만약 모든 아이템을 먹지 못했다면 0을 반환
"""
from sys import stdin

# 빈칸: 0, 아이템: 1, 벽: 2
def main():
    H, W, A, B = map(int, stdin.readline().split())
    board = [[0]*W for _ in range(H)]
    for _ in range(A):
        r, c = map(int, stdin.readline().split())
        board[H-r][c-1] = 1
    for _ in range(B):
        r, c = map(int, stdin.readline().split())
        board[H-r][c-1] = 2
    dp = [[0, 0] for _ in range(W+1)]
    dp[1][0] = 1
    for row in range(H-1, -1, -1):
        new_dp = [[0, 0] for _ in range(W+1)]
        for col in range(W):
            if board[row][col]==2:
                continue
            item = board[row][col]
            if new_dp[col][1]==dp[col+1][1]:
                new_dp[col+1] = [new_dp[col][0]+dp[col+1][0], new_dp[col][1]+item]
            elif new_dp[col][1]>dp[col+1][1]:
                new_dp[col+1] = [new_dp[col][0], new_dp[col][1]+item]
            else:
                new_dp[col+1] = [dp[col+1][0], dp[col+1][1]+item]
        dp = new_dp
    
    print(dp[-1][0] if dp[-1][1]==A else 0)

main()
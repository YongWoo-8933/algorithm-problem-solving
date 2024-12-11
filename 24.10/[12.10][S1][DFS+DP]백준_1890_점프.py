"""
백준 1890 점프 (실버1)

1. 동물원을 한줄일때부터 쭉 dp로 계산하면됨
"""
from sys import stdin

def main():
    N = int(stdin.readline())
    MAP = [[*map(int, i.split())] for i in stdin]
    dp = [[None]*N for _ in range(N)]
    dp[N-1][N-1] = 1
    
    def dfs(row: int, col: int) -> int:
        movable = MAP[row][col]
        cnt = 0
        for move in range(1, movable+1):
            for nrow, ncol in [(row+move, col), (row, col+move)]:
                if nrow<N and ncol<N:
                    if dp[nrow][ncol] is None:
                        dp[nrow][ncol] = dfs(nrow, ncol)
                    cnt += dp[nrow][ncol]
        return cnt
    
    print(dfs(0, 0))


main()

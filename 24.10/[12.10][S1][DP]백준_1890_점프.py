"""
백준 1890 점프 (실버1)

* 오른쪽, 아래쪽으로만 이동 가능하다면 FS 시리즈가 아니라 DP로 가야한다
1. DP로 갈 수 있는곳만 카운트
"""
from sys import stdin

def main():
    N = int(stdin.readline())
    MAP = [[*map(int, i.split())] for i in stdin]
    dp = [[0]*N for _ in range(N)]
    dp[0][0] = 1
    for row in range(N):
        for col in range(N):
            move_distance = MAP[row][col]
            if move_distance:
                for (nrow, ncol) in [(row+move_distance, col), (row, col+move_distance)]:
                    if nrow<N and ncol<N:
                        dp[nrow][ncol] += dp[row][col]
    
    print(dp[N-1][N-1])

main()

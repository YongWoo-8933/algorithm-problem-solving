"""
백준 1937 욕심쟁이 판다 (골드3)

1. DFS + DP로 풀어내면 됨
2. 각 칸에서 DFS를 시작하는데, DP 테이블에 각 칸에서 먹을 수 있는
   최대 대나무의 수를 저장함
"""
from sys import stdin, setrecursionlimit

def dfs(row: int, col: int) -> int:
    global woods, dp, N, d_xy
    if not dp[row][col]:
        result = 1
        for dx, dy in d_xy:
            nrow, ncol = row+dy, col+dx
            if 0<=nrow<N and 0<=ncol<N and woods[row][col]<woods[nrow][ncol]:
                result = max(result, dfs(nrow, ncol)+1)
        dp[row][col] = result
    return dp[row][col]

setrecursionlimit(10**6)
N = int(stdin.readline())
woods = [[*map(int, i.split())] for i in stdin]
dp = [[None]*N for _ in range(N)]
answer = 0
d_xy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for row in range(N):
    for col in range(N):
        if not dp[row][col]:
            answer = max(answer, dfs(row, col))
print(answer)
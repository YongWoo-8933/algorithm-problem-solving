"""
백준 25343 최장 최장 증가 부분 수열 (골드5)
* 실행시간이 너무 길어서 다시 품

<풀이 1>
1. N*N*10,001 크기의 dp table을 만듦
2. dp에는 i행 j열까지 나올 수 있는 최장수열의 길이(cnt)를 저장
3. 저장할때 해당 최장수열의 마지막 값이 x일 경우, dp[i][j][x]에 저장함
4. dp의 N행 N열 리스트에서 가장 큰값이 최장 최장수열의 길이가 됨
-> 이 방법은 보드 위 원소값이 1~10000의 범위이기 때문에 가능함.
-> 원소값이 더 커질수 있다면 시간초과

<풀이 2>
1. N*N 크기의 dp table을 만듦
2. row행 col열에 대해 모두 다음 로직을 수행
3. row행~N-1행, col열~N-1열 까지 for문을 돌림. 각각 nrow와 ncol이라 하자.
4. 만약 보드의 row행 col열 값보다 nrow행 ncol열 값이 더 큰경우
   dp[nrow][ncol] 값을 dp[nrow][ncol]값과 dp[row][col]값중 큰 값으로 갱신
5. dp table의 모든 값중 가장 큰값을 리턴
"""
from sys import stdin  

# 1차 풀이 - 2,568ms
N = int(stdin.readline())
board = [[*map(int, i.split())] for i in stdin]
dp = [[[0]*10001 for _ in range(N+1)] for __ in range(N+1)]
for row in range(N):
    for col in range(N):
        x = board[row][col]
        for temp in [dp[row+1][col], dp[row][col+1]]:
            for max_value, cnt in enumerate(temp):
                if cnt:
                    dp[row+1][col+1][max_value] = max(dp[row+1][col+1][max_value], cnt)
                    if max_value<x:
                        dp[row+1][col+1][x] = max(dp[row+1][col+1][x], cnt+1)
        dp[row+1][col+1][x] = max(dp[row+1][col+1][x], 1)
print(max(dp[N][N]))

# 2차 풀이 - 888ms
N = int(stdin.readline())
board = [[*map(int, i.split())] for i in stdin]
dp = [[1]*N for _ in range(N)]
for row in range(N):
    for col in range(N):
        for nrow in range(row, N):
            for ncol in range(col, N):
                if board[row][col]<board[nrow][ncol]:
                    dp[nrow][ncol] = max(dp[nrow][ncol], dp[row][col]+1)
print(max(max(dp[i]) for i in range(N)))
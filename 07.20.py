"""
백준 11066 파일 합치기 (골드3)

풀이 1. O(N^3) 행렬 dp풀이 
(https://velog.io/@seung_min/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-11066%EB%B2%88-%ED%8C%8C%EC%9D%BC-%ED%95%A9%EC%B9%98%EA%B8%B0)

풀이 2. O(N^2) 크누스 알고리즘(Knuth Optimization)
(https://blog.naver.com/hands731/221809346951)
"""
from sys import stdin

def sol1(n: int, lst: list) -> int:
    dp = [[0]*n for _ in range(n)]
    sum_dp = [0, lst[0]]
    for i in range(1, n):
        dp[i-1][i] = lst[i-1]+lst[i]
        sum_dp.append(sum_dp[-1]+lst[i])
    for i in range(2, n):
        for j in range(n-i):
            dp[j][j+i] = min(dp[j][j+k]+dp[j+k+1][j+i] for k in range(i))+sum_dp[j+i+1]-sum_dp[j]
    return dp[0][n-1]

def sol2(n: int, lst: list) -> int:
    dp = [[0]*n for _ in range(n)]
    sum_dp = [0]
    knuth = [[0]*n for _ in range(n)]
    for i in range(n):
        knuth[i][i] = i
        sum_dp.append(sum_dp[-1]+lst[i])
    for i in range(1, n):
        for j in range(n-i):
            min_value = float('inf')
            for k in range(knuth[j][j+i-1], min(knuth[j+1][j+i]+1, j+i)):
                x = dp[j][k]+dp[k+1][j+i]
                if x<min_value:
                    min_value = x
                    knuth[j][j+i] = k
            dp[j][j+i] = min_value+sum_dp[j+i+1]-sum_dp[j]
    return dp[0][n-1]

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    lst = [*map(int, stdin.readline().split())]
    # print(sol1(N, lst, make_sum_dp(N, lst)))
    print(sol2(N, lst))

"""
백준 15486 퇴사 2 (골드5)

1. dp로 진행. dp[i]에는 i번째 날짜 이후 얻을 수 있는 최대 금액을 저장
2. 뒤에서부터 거꾸로 dp 테이블 제작 -> 현재 상담을 넣었을때 vs 넣지 않았을때 비교
"""

from sys import stdin

def main():
    N = int(stdin.readline())
    lst = [[*map(int, i.split())] for i in stdin]
    dp = [0]*(N+1)
    for i in range(N-1, -1, -1):
        day, price = lst[i]
        if i+day-1<N:
            dp[i] = max(price+dp[i+day], dp[i+1])
        else:
            dp[i] = dp[i+1]
    print(dp[0])

main()

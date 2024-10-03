"""
백준 30460 스위치 (골드 5)

** 실전에서는 종이에 충분히 그려보고 풀자 **
1. 다익스트라인줄 알았으나 간단한 dp로 풀림
2. 조금만 그려보면 점화식을 찾을 수 있음
"""

def main():
    N = int(input())
    lst = [*map(int, input().split())]
    dp1, dp2, dp3 = lst[2], lst[1]+lst[2], max(lst[0]+lst[1]+lst[2], 0)
    for i in range(3, N):
        x = lst[i]
        dp1, dp2, dp3 = dp3+x, dp1+x, max(dp2+x, dp3)
    print(max(dp1, dp2, dp3)+sum(lst))
main()
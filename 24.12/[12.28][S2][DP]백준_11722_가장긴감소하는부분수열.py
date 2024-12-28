"""
백준 11722 가장 긴 감소하는 부분 수열 (실버2)

1. 수열을 역순으로 두고 LIS 진행행
"""
from bisect import bisect_left

def main():
    input()
    lst = [*map(int, input().split())]
    LIS = []
    for n in lst[::-1]:
        idx = bisect_left(LIS, n)
        if len(LIS)==idx:
            LIS.append(n)
        else:
            LIS[idx] = n
    print(len(LIS))

main()
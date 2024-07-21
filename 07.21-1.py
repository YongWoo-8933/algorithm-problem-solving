"""
백준 9465 스티커 (실버1)

1. dp 테이블 두개 운영(각 자리의 스티커를 붙였을때 최대값 저장)
2. 전 열과 전전 열에서 반대쪽 스티커를 선택할 경우를 비교해 
   더 큰값을 택하고 해당자리 스티커를 선택
"""
from sys import stdin

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    stickers = [[*map(int, stdin.readline().split())] for __ in range(2)]
    dp_a, dp_b = [0]*(N+2), [0]*(N+2)
    for i in range(2, N+2):
        a, b = stickers[0][i-2], stickers[1][i-2]
        dp_a[i] = max(dp_b[i-1], dp_b[i-2])+a
        dp_b[i] = max(dp_a[i-1], dp_a[i-2])+b
    print(max(dp_a[-2], dp_a[-1], dp_b[-2], dp_b[-1]))

"""
백준 12015 가장 긴 증가하는 부분 수열 2

** LIS 알고리즘 개념필요 (https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4)
1. dp table 생성, dp table의 (i+1)번째 원소는 '길이가 (i+1)인 증가하는 수열중 가장 큰 값'으로 정의함
2. 수열의 각 원소에 대해 for문 진입, 원소 n이 dp의 마지막 원소(현재 가장 긴 길이를 가지는 수열의 가장 큰값)
   보다 크다면, dp에 n 추가
3. 그렇지 않다면 이진탐색으로 n이 dp에서 몇번째에 들어가는지 찾아 갱신
"""
from bisect import bisect_left
input()
dp = [0]
for n in map(int, input().split()):
    if n>dp[-1]:
        dp.append(n)
    else:
        idx = bisect_left(dp, n)
        dp[idx] = n
print(len(dp)-1)





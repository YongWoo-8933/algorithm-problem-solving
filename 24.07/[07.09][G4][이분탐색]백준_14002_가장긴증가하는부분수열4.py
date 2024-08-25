"""
백준 14002 가장 긴 증가하는 부분 수열 4 (골드4)

1. 가장 긴 증가하는 부분수열의 이분탐색 풀이법을 그대로 사용
2. 단, 수열 자체를 저장해놓기위해 길이별로(1~1000)
   증가하는 부분수열을 따로 저장해놓음
"""
from bisect import bisect_left
from copy import deepcopy

N = int(input())
lst = [*map(int, input().split())]
dp = [lst[0]]
answer = [[lst[0]]]
for x in lst[1:]:
    idx = bisect_left(dp, x)
    temp = deepcopy(answer[idx-1]) if idx!=0 else []
    temp.append(x)
    if idx==len(dp):
        dp.append(x)
        answer.append(temp)
    else:
        dp[idx] = x
        answer[idx] = temp
print(len(answer[-1]))
print(*answer[-1])






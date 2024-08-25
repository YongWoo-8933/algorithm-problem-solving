"""
백준 7579 앱 (골드3)

1. 배낭문제(dp)와 유형이 같아보임
2. 발생할 수 있는 cost가 0~10000까지로 정해져 있으므로, 각 cost별 최대 memory를 갱신하는 식으로 진행
3. cost-memory set을 lst로 저장후, cost순으로 정렬하고 진행
"""
N, M = map(int, input().split())
lst = [(c, m) for m, c in zip(map(int, input().split()), map(int, input().split()))]
lst.sort(key=lambda x: x[0])
dp = [0]*10001
for i in range(N):
   cost, memory = lst[i]
   for c, m in [(i, dp[i]) for i in range(10001) if dp[i]]:
      dp[c+cost] = max(dp[c+cost], m+memory)
   dp[cost] = max(dp[cost], memory)
for i in range(10001):
   if dp[i] >= M:
      print(i)
      exit()










"""
백준 13913 숨바꼭질 4 (골드4)

1. 경로에 주의하여 dp를 통한 BFS 진행
"""
from heapq import heappop, heappush

N, K = map(int, input().split())
if K<=N:
    print(N-K)
    print(*range(N, K-1, -1))
    exit()
dp = [(10**6, 0)]*(K+2)
dp[N] = (0, 0)
hq = [(0, N)]
while hq:
    cnt, num = heappop(hq)
    if num==K:
        break
    n_cnt = cnt+1
    for n_num in (num-1, num+1, 2*num):
        if 0<=n_num<K+2 and n_cnt<dp[n_num][0]:
            dp[n_num] = (n_cnt, num)
            heappush(hq, (n_cnt, n_num))

answer_cnt, n = dp[K]
answer_history = [K, n]
while n!=N:
    _, n = dp[n]
    answer_history.append(n)
print(answer_cnt)
print(*reversed(answer_history))
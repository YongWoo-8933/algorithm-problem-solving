"""
백준 14715 전생했더니 슬라임 연구자였던 건에 대하여 (Easy) (골드5)

1. 먼저 에라토스테네스의 체 알고리즘으로 K 이하 소수 모두 구하기
2. 크기가 K+1인 dp table 생성 
   -> dp의 i번째 원소는 피가 i인 슬라임을 분할했을때의 답
3. dp의 i값이 소수인 경우 분할이 안되므로 모두 0으로 초기화
4. dp의 i값이 소수가 아닌경우, 약수 j와 i//j값에 대해 재귀적으로 dp[j], dp[i//j]값을 갱신함.
5. i의 모든 약수에 대해 dp 테이블을 갱신했다면, 어떤 약수조합이 흉터가 최소가 되는지 구해 dp[i] 갱신
"""
K = int(input())
prime = [True]*(K+1)
prime[1] = False

for i in range(2, K+1):
    if prime[i]==True:
        j = 2
        while i*j<=K:
            prime[i*j] = False
            j += 1

dp = [0 if prime[i] else None for i in range(K+1)]

def f(n: int):
    global dp
    if dp[n] is None:
        min_value = float("inf")
        j = 2
        while j*j<=n:
            if n%j==0:
                f(j)
                f(n//j)
                min_value = min(min_value, max(dp[j], dp[n//j])+1)
            j += 1
        dp[n] = min_value

f(K)

print(dp[-1])
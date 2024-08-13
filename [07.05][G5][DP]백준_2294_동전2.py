"""
백준 2294 동전2 (골드5)

1. 가치가 1~K일때 필요한 동전의 최소값을 저장할 dp table 작성, -1로 초기화
2. 가치가 K이하인 동전만 따로 저장
3. dp table에서 가치가 coin값과 같은 경우 1개로 초기값 설정
4. dp의 각 가치에 대해 coin을 한개씩 더해보며 dp table의 다음 값 갱신
5. 순회가 끝나면 dp[K]값 출력(만들 수 없다면 초기값인 -1 출력됨)
"""
from sys import stdin

N, K = map(int, stdin.readline().split())
coins = [int(i) for i in stdin if int(i)<=K]
dp = [-1]*(K+1)
for coin in coins:
    dp[coin] = 1
for value in range(1, K+1):
    if dp[value]>0:
        for coin in coins:
            if value+coin<=K:
                if dp[value+coin]>0:
                    dp[value+coin] = min(dp[value+coin], dp[value]+1)
                else:
                    dp[value+coin] = dp[value]+1
print(dp[K])















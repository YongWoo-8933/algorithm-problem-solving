"""
백준 14628 입 챌린저(골드3)

1. hp가 0일때부터 M일때까지 필요한 최소 마나의 양을 dp로 기록해나감
2. hp별 dp table 요소에는 해당 최소 마나를 이루기까지 사용한 각 스킬의 개수를 저장해놓음, 이를통해 마나 계산 
"""
from sys import stdin

def main():
    N, M, K = map(int, stdin.readline().split())
    skills = [[*map(int, i.split())] for i in stdin]
    dp = [[None, [0]*N] for _ in range(M+1)]
    dp[0][0] = 0
    for hp in range(M):
        for idx in range(N):
            mana, damage = skills[idx]
            new_hp = hp+damage
            if dp[hp][0] is not None and new_hp<=M:
                new_mana = dp[hp][0]+mana+dp[hp][1][idx]*K
                if dp[new_hp][0] is None or new_mana<dp[new_hp][0]:
                    new_usage = dp[hp][1].copy()
                    new_usage[idx] += 1
                    dp[new_hp] = [new_mana, new_usage]
    print(dp[-1][0])

main()

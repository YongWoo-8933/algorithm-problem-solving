"""
백준 17404 RGB거리 2

1. RGB거리 1 문제와 똑같이 dp로 접근, 다만 조건이 추가됐으므로 시작색깔이 다른 dp테이블 세개를 활용
2. 1, 2번째 값까지 갱신된 dp table 생성(성립할 수 없는 경우 무한대의 비용 산정)
3. 3번째 이상의 순서에서는 각각 dp table을 갱신하고, 마지막 N번째 경우만 따로 계산
4. 각 dp table에서 최소비용을 찾아 출력
"""
from sys import stdin
N = int(stdin.readline())
costs = [[*map(int, i.split())] for i in stdin]
dp_R = [float("inf"), costs[0][0]+costs[1][1], costs[0][0]+costs[1][2]]
dp_G = [costs[0][1]+costs[1][0], float("inf"), costs[0][1]+costs[1][2]]
dp_B = [costs[0][2]+costs[1][0], costs[0][2]+costs[1][1], float("inf")]
if N>2:
    for cost_R, cost_G, cost_B in costs[2:N-1]:
        dp_R = [min(dp_R[1], dp_R[2])+cost_R, min(dp_R[0], dp_R[2])+cost_G, min(dp_R[0], dp_R[1])+cost_B]
        dp_G = [min(dp_G[1], dp_G[2])+cost_R, min(dp_G[0], dp_G[2])+cost_G, min(dp_G[0], dp_G[1])+cost_B]
        dp_B = [min(dp_B[1], dp_B[2])+cost_R, min(dp_B[0], dp_B[2])+cost_G, min(dp_B[0], dp_B[1])+cost_B]
    dp_R = [float("inf"), min(dp_R[0], dp_R[2])+costs[-1][1], min(dp_R[0], dp_R[1])+costs[-1][2]]
    dp_G = [min(dp_G[1], dp_G[2])+costs[-1][0], float("inf"), min(dp_G[0], dp_G[1])+costs[-1][2]]
    dp_B = [min(dp_B[1], dp_B[2])+costs[-1][0], min(dp_B[0], dp_B[2])+costs[-1][1], float("inf")]
print(min(min(dp_R), min(dp_G), min(dp_B)))


    


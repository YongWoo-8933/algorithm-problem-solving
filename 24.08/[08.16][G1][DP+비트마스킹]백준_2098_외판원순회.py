"""
백준 2098 외판원 순회 (골드1)

1. 비트마스킹 개념을 제대로 이해하고 dp로 풀어야함.
2. 비트마스킹 개념 링크: https://e-juhee.tistory.com/entry/python-%EB%B0%B1%EC%A4%80-2098-%EC%99%B8%ED%8C%90%EC%9B%90-%EC%88%9C%ED%9A%8C-DP-%EB%B9%84%ED%8A%B8%EB%A7%88%EC%8A%A4%ED%82%B9
3. 위 풀이와는 다르게, dp[node][bits] 안에 각 노드와 비트 상황에서 
   이후 방문들의 최소비용값을 재귀로 구해 저장하도록 했음.
"""
from sys import stdin

def dfs(node: int, bits: int) -> int:
    global N, INF, costs, dp
    if dp[node][bits] is None:
        if bits==2**N-1:
            dp[node][bits] = costs[node][0] if costs[node][0] else INF
        else:
            min_cost = INF
            for next_node in range(N):
                if costs[node][next_node]!=0 and bits&(1<<next_node)==0:
                    x = dfs(next_node, bits|(1<<next_node))
                    min_cost = min(min_cost, costs[node][next_node]+x)
            dp[node][bits] = min_cost
    return dp[node][bits]

N = int(stdin.readline())
costs = [[*map(int, i.split())] for i in stdin]
INF = 1000000*16
dp = [[None]*(2**N) for _ in range(N)]
print(dfs(0, 1))
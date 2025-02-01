"""
백준 2132 나무 위의 벌레 (골드3)

1. dfs로 각 간선으로 향할때 최대 먹을 수 있는 열매 수를 저장
2. 모든 노드에 대해 dfs를 돌려 열매의 최대 수 찾기기
"""
from sys import stdin, setrecursionlimit

def main():
    setrecursionlimit(10**6)
    N = int(stdin.readline())
    fruits = [0, *map(int, stdin.readline().split())]
    dp = [dict() for _ in range(N+1)]
    for i in stdin:
        fr, to = map(int, i.split())
        dp[fr][to] = None
        dp[to][fr] = None

    def dfs(node: int, from_node: int) -> int:
        result = 0
        for next_node, max_cnt in dp[node].items():
            if next_node!=from_node:
                if max_cnt is None:
                    dp[node][next_node] = dfs(next_node, node)
                result = max(result, dp[node][next_node])
        return fruits[node]+result

    answer_cnt, answer_node = 0, 1
    for node in range(1, N+1):
        result = dfs(node, 0)
        if result>answer_cnt:
            answer_cnt, answer_node = result, node
    print(answer_cnt, answer_node)

main()
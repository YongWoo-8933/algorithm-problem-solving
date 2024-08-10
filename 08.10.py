"""
백준 10159 저울 (골드 4)

1. 평범한 시뮬레이션 문제
2. 구름 이동 시 각 끝부분이 연결되도록 N으로 나눈 나머지 값으로 설정
3. 구름이 사라진 칸에 새 구름이 생기지 않도록 기억해두기(cloud_map 운영)
"""
from sys import stdin
from collections import deque

N, _ = int(stdin.readline()), int(stdin.readline())
links = [set() for _ in range(N+1)]
indegrees = [0]*(N+1)
for i in stdin:
    h, l = map(int, i.split())
    links[l].add(h)
    indegrees[h] += 1

for s_node in range(1, N+1):

for s_node in range(1, N+1):
    answer = -1
    answer += dfs(s_node, heavy_links)
    answer += dfs(s_node, light_links)
    print(N-answer)



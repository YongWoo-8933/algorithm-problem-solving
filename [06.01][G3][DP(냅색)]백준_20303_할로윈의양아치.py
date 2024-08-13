"""
백준 20303 할로윈의 양아치

1. DFS로 각 친구집합의 총 캔디수와 인원수를 answer에 tuple 형태로 저장
2. 냅색(배낭문제) 알고리즘으로 사탕을 뺏은 학생수별 얻을 수 있는 최대 사탕수를 갱신
"""
from sys import stdin, setrecursionlimit

setrecursionlimit(10**5)
input = stdin.readline
N, _, K = map(int, input().split())
candies = [0, *map(int, input().split())]
links = [set() for _ in range(N+1)]
for i in stdin:
   fr, to = map(int, i.split())
   links[fr].add(to)
   links[to].add(fr)
visited = [0]*(N+1)
answer = []

def dfs(node: int):
   global total_candy, children, visited, candies, links, K
   children += 1
   total_candy += candies[node]
   for next_node in links[node]:
      if not visited[next_node]:
         visited[next_node] = 1
         dfs(next_node)

for start_node in range(1, N+1):
   if not visited[start_node]:
      total_candy, children = 0, 0
      visited[start_node] = 1
      dfs(start_node)
      if children<K:
         answer.append((total_candy, children))

dp = [0]*K
for candy, children in answer:
   for i in range(K-1, -1, -1):
      if dp[i] and i+children<K:
         dp[i+children] = max(dp[i+children], dp[i]+candy)
   dp[children] = max(dp[children], candy)
print(max(dp))
         










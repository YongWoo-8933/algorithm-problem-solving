"""
백준 16724 피리 부는 사나이 (골드3)

1. DFS로 사이클의 갯수를 세면 됨
2. 주의할점은 사이클이 생성되어 DFS가 종료되는 경우와,
   기존에 방문했던 사이클을 다시 방문해 DFS가 종료되는 경우를 구분해줘야한다는 것
3. route라는 set으로 해당 DFS탐사중 방문했던 노드를 기억해 두 경우를 구분했음
"""
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
input = stdin.readline
H, W = map(int, input().split())
MAP = [i.strip() for i in stdin]
visited = [[0]*W for _ in range(H)]
answer = 0

def dfs(route: set, row: int, col: int):
   global MAP, H, W, visited, answer
   if visited[row][col]:
      if (row, col) in route:
         answer += 1
   else:
      visited[row][col] = 1
      route.add((row, col))
      d = MAP[row][col]
      dx, dy = [0, 0, -1, 1]["UDLR".index(d)], [-1, 1, 0, 0]["UDLR".index(d)]
      dfs(route, row+dy, col+dx)

for row in range(H):
   for col in range(W):
      if visited[row][col]==0:
         dfs(set(), row, col)

print(answer)
         










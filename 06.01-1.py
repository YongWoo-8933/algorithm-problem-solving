"""
백준 9466 텀 프로젝트 

1. 사이클의 발생여부를 파악하는 문제 
   -> DFS 진행하다가 방문했던 노드를 발견하면 사이클이라고 판정
2. 사이클에 속하지 않는 노드의 갯수를 출력
"""
from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10**6)

def dfs(route_lst: list, route_set: set):
      global visited, answer, parent
      node = route_lst[-1]
      if visited[node]:
         answer += len(route_lst)-1
      else:
         visited[node] = 1
         parent_node = parent[node]
         if parent_node in route_set:
            answer += route_lst.index(parent_node)
         else:
            route_lst.append(parent_node)
            route_set.add(parent_node)
            dfs(route_lst, route_set)

for _ in range(int(input())):
   N = int(input())
   parent = [0, *map(int, input().split())]
   visited = [0]*(N+1)
   answer = 0
   
   for i in range(1, N+1):
      if visited[i]==0:
         dfs([i], {i})

   print(answer)









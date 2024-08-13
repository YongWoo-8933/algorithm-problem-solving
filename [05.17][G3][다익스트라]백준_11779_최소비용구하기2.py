"""
백준 11779 최소비용 구하기 2 (골드3)

1. 다익스트라 알고리즘 구현
2. heapq를 통해 비용이 적은 경우부터 계산
3. check를 통해 최소 비용을 갱신할 때, (최소비용, 직전노드) 의 튜플형식으로 저장
4. check에서 도착지 최소비용을 산출하고, 직전 노드로 거슬러 올라가며 경로를 산출
"""
from sys import stdin
from heapq import heappop, heappush

N, M = int(stdin.readline()), int(stdin.readline())
links = [set() for _ in range(N+1)]
for _ in range(M):
    fr, to, cost = map(int, stdin.readline().split())
    links[fr].add((to, cost))
start_node, end_node = map(int, stdin.readline().split())
q = [(0, start_node)]
check = [[10**9, 0] for _ in range(N+1)]
check[start_node][0] = 0
while q:
    total_cost, node = heappop(q)
    if node == end_node:
        continue
    for next_node, next_cost in links[node]:
        if total_cost+next_cost < check[next_node][0]:
            check[next_node][0], check[next_node][1] = total_cost+next_cost, node
            heappush(q, (total_cost+next_cost, next_node))
route = [end_node]
previous_node = check[end_node][1]
while previous_node:
    route.append(previous_node)
    previous_node = check[previous_node][1]
print(check[end_node][0], len(route))
print(*route[::-1])

    


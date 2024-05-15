"""
백준 14938 서강그라운드

1. BFS를 통한 완전탐색
2. 간선 정보를 통해 연결관계를 정의하는 리스트 links 작성
3. 각 노드를 시작점으로 하는 BFS 구현
4. check 리스트에서 각 노드로 통하는 최소 거리를 갱신하며 경우 탐색
5. 방문한 노드는 모두 set에 추가하고, 마지막에 방문한 노드의 아이템값의 합을 산출
"""
from collections import deque
from sys import stdin
 
N, dist_limit, _ = map(int, stdin.readline().split())
items = [0, *map(int, stdin.readline().split())]
links = [set() for _ in range(N+1)]
for i in stdin:
    fr, to, dist = map(int, i.split())
    links[fr].add((to, dist))
    links[to].add((fr, dist))
max_item = 0
for start_node in range(1, N+1):
    q = deque([(0, start_node)])
    check = [dist_limit] * (N+1)
    check[start_node] = 0
    nodes = set()
    while q:
        total_dist, node = q.popleft()
        nodes.add(node)
        for next_node, next_dist in links[node]:
            if total_dist+next_dist <= check[next_node]:
                check[next_node] = total_dist+next_dist
                q.append((total_dist+next_dist, next_node))
    max_item = max(max_item, sum(items[i] for i in nodes))
print(max_item)



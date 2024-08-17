"""
백준 28333 화이트칼라 (골드4)

1. BFS 모든 최단경로의 노드를 구하는 문제
2. 각 노드에 방문할 때, 최단 이동거리를 visited에 저장해 그 이상값은 무시
3. 동시에, 어느 노드에서 왔는지 정보를 reverse_links에 저장
4. visited에 저장된 최단거리값이 갱신되는 경우, reverse_links역시 갱신
5. visited에 저장된 최단거리값과 같은 값인 경우, reverse_links에 해당 노드를 추가
6. BFS종료 후 reverse_links에 저장된 경로 정보를 토대로 도착 노드에서 
   거꾸로 BFS를 돌리며 최단 경로에 해당하는 모든 노드를 answer에 추가함
7. answer를 오름차순 정렬해 출력
"""
from sys import stdin
from collections import deque

input = stdin.readline
INF = 10**4
for _ in range(int(input())):
    N, M = map(int, input().split())
    links = [set() for _ in range(N+1)]
    reverse_links = [set() for _ in range(N+1)]
    for __ in range(M):
        fr, to = map(int, input().split())
        links[fr].add(to)
    visited = [INF]*(N+1)
    visited[1] = 1
    q = deque([(1, 1)])
    while q:
        cnt, node = q.popleft()
        for next_node in links[node]:
            if cnt+1<visited[next_node]:
                visited[next_node] = cnt+1
                reverse_links[next_node] = {node}
                q.append((cnt+1, next_node))
            elif cnt+1==visited[next_node]:
                reverse_links[next_node].add(node)
    answer = {N}
    q = deque([N])
    while q:
        node = q.popleft()
        for next_node in reverse_links[node]:
            if next_node not in answer:
                answer.add(next_node)
                q.append(next_node)
    print(*sorted(answer))
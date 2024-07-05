"""
백준 1707 이분 그래프 (골드4)

1. 노드의 연결관계를 저장해놓음
2. 아무노드에서나 BFS를 돌기 시작함
3. 두 개의 그룹을 운영하며, 현재 노드와 직접 연결된 노드들을 모두 반대편 그룹에 추가
4. 직접 연결된 노드가 이미 자신의 그룹에 추가되어 있다면 "NO" 출력
5. ** 모든 노드가 연결되어 있지 않을 가능성이 있음
      따라서 순회하지 않은 노드가 있다면 위 작업을 계속 반복
6. 모든 노드를 순회했는데 4번 경우가 발생하지 않았다면 "YES" 출력
"""
from sys import stdin
from collections import deque

for _ in range(int(stdin.readline())):
    N, V = map(int, stdin.readline().split())
    links = [set() for _ in range(N+1)]
    for __ in range(V):
        fr, to = map(int, stdin.readline().split())
        links[fr].add(to)
        links[to].add(fr)

    groups = [set(), set()]
    answer = "YES"
    s_nodes = {i for i in range(1, N+1)}
    while s_nodes and answer=="YES":
        q = deque([(0, s_nodes.pop())])
        while q and answer=="YES":
            g_idx, node = q.popleft()
            if node in s_nodes:
                s_nodes.remove(node)
            next_g_idx = 0 if g_idx else 1
            for next_node in links[node]:
                if next_node in groups[g_idx]:
                    answer = "NO"
                elif next_node in groups[next_g_idx]:
                    continue
                else:
                    groups[next_g_idx].add(next_node)
                    q.append((next_g_idx, next_node))
    print(answer)














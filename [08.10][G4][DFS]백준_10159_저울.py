"""
백준 10159 저울 (골드 4)

1. 무게 비교로 node간 연결이 만들어질때, 무거운/가벼운 방향에 따라 단방향 링크를 저장
2. 특정 노드에서 무거운 방향, 가벼운 방향으로 dfs를 진행했을때 만나는 노드들은
   모두 무게를 비교할 수 있는 노드들이므로 이 수를 카운트
3. 전체 노드수에서 카운트한 수를 빼주면 비교할 수 없는 노드의 수가 나옴
"""
from sys import stdin

def dfs1(node: int) -> int:
    global heavy_links, visited1
    cnt = 1
    for next_node in heavy_links[node]:
        if not visited1[next_node]:
            visited1[next_node] = True
            cnt += dfs1(next_node)
    return cnt

def dfs2(node: int) -> int:
    global light_links, visited2
    cnt = 1
    for next_node in light_links[node]:
        if not visited2[next_node]:
            visited2[next_node] = True
            cnt += dfs2(next_node)
    return cnt

N, _ = int(stdin.readline()), int(stdin.readline())
heavy_links, light_links = [set() for _ in range(N+1)], [set() for _ in range(N+1)]
for i in stdin:
    h, l = map(int, i.split())
    heavy_links[l].add(h)
    light_links[h].add(l)
for s_node in range(1, N+1):
    answer = -1
    visited1, visited2 = [False]*(N+1), [False]*(N+1)
    visited1[s_node] = True
    visited2[s_node] = True
    answer += dfs1(s_node)
    answer += dfs2(s_node)
    print(N-answer)



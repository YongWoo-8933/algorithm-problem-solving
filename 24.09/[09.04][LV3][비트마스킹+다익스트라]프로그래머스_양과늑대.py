"""
프로그래머스 양과 늑대 (LV3)

1. 트리를 평범한 graph로 생각하고 각 노드의 연결상태를 links에 정리
2. BFS를 진행하는데, 방문 여부를 파악하는 방법에 비트마스킹+다익스트라 활용
   방문했던 노드를 10010001 이런식으로 되어있을때 가지고 있는 양의 수중 최고값을
   visited[node][비트값]에 저장하는 식
3. 이후로는 다익스트라 방식과 똑같이 진행하면됨
4. BFS가 끝나면 visited의 루트노드에서 가장 양의 수가 많은 값을 리턴
"""
from collections import deque

def solution(info, edges):
    N = len(info)
    links = [set() for _ in range(N)]
    for parent, child in edges:
        links[parent].add(child)
        links[child].add(parent)
    visited = [{} for _ in range(N)]
    visited[0][1] = 1
    q = deque([(0, 1, 0, 1)])
    while q:
        node, sheep, wolves, bit = q.popleft()
        for new_node in links[node]:
            new_bit = bit | (1<<new_node)
            new_sheep, new_wolves = sheep, wolves
            # 해당 노드 방문한적이 없음 -> 양 늑대 갱신
            if bit != new_bit:
                if info[new_node]==0:
                    new_sheep += 1
                elif sheep>wolves+1:
                    new_wolves += 1
                else:
                    continue
            if new_bit not in visited[new_node]:
                visited[new_node][new_bit] = new_sheep
                q.append((new_node, new_sheep, new_wolves, new_bit))
            elif new_sheep>visited[new_node][new_bit]:
                visited[new_node][new_bit] = new_sheep
                q.append((new_node, new_sheep, new_wolves, new_bit))
    return max(visited[0].values())
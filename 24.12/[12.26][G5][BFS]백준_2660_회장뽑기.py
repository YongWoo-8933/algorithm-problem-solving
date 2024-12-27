"""
백준 2660 회장뽑기 (골드5)

1. 간단한 bfs로 노드간 거리 검사
"""
from sys import stdin
from collections import deque

def main():
    N = int(stdin.readline())
    links = [set() for _ in range(N+1)]
    for i in stdin:
        a, b = map(int, i.split())
        if a<0 and b<0:
            break
        links[a].add(b)
        links[b].add(a)
    answer_nodes, answer_score = [], 50
    for node in range(1, N+1):
        visited = [False]*(N+1)
        visited[node] = True
        score = 0
        q = deque([(0, node)])
        while q:
            cur_score, cur_node = q.popleft()
            score = max(cur_score, score)
            for next_node in links[cur_node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    q.append((cur_score+1, next_node))
        if score<answer_score:
            answer_score = score
            answer_nodes = [node]
        elif score==answer_score:
            answer_nodes.append(node)
    print(answer_score, len(answer_nodes))
    print(*sorted(answer_nodes))

main()
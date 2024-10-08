"""
백준 9470 Strahler 순서 (골드3)

1. 위상정렬로 특정 노드로 흘러들어오는 모든 강의 order가 정해진 후 실행되도록함
2. 따로 자료구조를 활용해 해당 노드로 들어오는 강의 order 최대값과 그 수를 저장
3. 마지막 강의 순서 return
"""
from sys import stdin
from collections import deque

def main():
    for _ in range(int(stdin.readline())):
        K, M, P = map(int, stdin.readline().split())
        indegrees = [[0] for _ in range(M+1)]
        links = [set() for _ in range(M+1)]
        for _ in range(P):
            fr, to = map(int, stdin.readline().split())
            links[fr].add(to)
            indegrees[to] += 1

        order = [1]*(M+1)
        indegree_max_order = [1]*(M+1)
        indegree_max_cnt = [0]*(M+1)
        q = deque()
        for i in range(1, M+1):
            if indegrees[i]==0:
                q.append(i)

        while q:
            node = q.popleft()
            for next_node in links[node]:
                indegrees[next_node] -= 1
                if indegree_max_order[next_node]==order[node]:
                    indegree_max_cnt[next_node] += 1
                elif indegree_max_order[next_node]<order[node]:
                    indegree_max_order[next_node] = order[node]
                    indegree_max_cnt[next_node] = 1

                if indegrees[next_node]==0:
                    q.append(next_node)
                    if indegree_max_cnt[next_node]>1:
                        order[next_node] = indegree_max_order[next_node]+1
                    else:
                        order[next_node] = indegree_max_order[next_node]
        print(K, order[M])

main()
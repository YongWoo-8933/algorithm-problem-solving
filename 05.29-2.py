"""
백준 2623 음악프로그램 

1. 사이클과 중복간선에 유의하여 위상정렬 실행
   - 중복간선은 무시
   - 정렬 시작 전, 진입차수 lst에 0인 값이 없을 때 사이클로 판단
   - 정렬 종료 후, 진입차수 lst에 0이 아닌 값이 있을때 사이클로 판단
   - 방문했던 노드에 다시 방문하는 경우 사이클로 판단
"""
from sys import stdin
from collections import deque
N, M = map(int, stdin.readline().split())
indegree = [0]*(N+1)
lst = [set() for _ in range(N+1)]
for i in stdin:
    l = [*map(int, i.split())]
    for j in range(2, l[0]+1):
        if l[j] not in lst[l[j-1]]:
            lst[l[j-1]].add(l[j])
            indegree[l[j]] += 1
q = deque()
for start_node in range(1, N+1):
    if indegree[start_node]==0:
        q.append(start_node)
if not q:
    print(0)
    exit()
answer = []
visited = set()
while q:
    node = q.popleft()
    answer.append(node)
    visited.add(node)
    for next_node in lst[node]:
        if next_node in visited:
            print(0)
            exit()
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            q.append(next_node)
if any(i!=0 for i in indegree):
    print(0)
    exit()
print(*answer)









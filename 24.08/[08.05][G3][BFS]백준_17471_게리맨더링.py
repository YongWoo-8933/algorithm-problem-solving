"""
백준 17471 게리맨더링 (골드3)

1. itertools의 combinations를 통해 선거구 node조합을 구함(N//2 만큼만 ex. 10명이면 5명 조합까지)
2. 구한 node 조합에 대해 BFS를 돌려 해당 노드들이 연결되어 있는지 확인
2-1. 연결되어 있지 않다면 다음 node조합 실행
3. 연결되어 있다면, 구한 node들을 제외한 나머지 node 조합에 대해 BFS 실행
3-1. 나머지 node조합이 연결되어 있지 않다면 다음 node 조합 실행
4. 나머지 node조합이 연결되어있다면, answer에 인구수 차이 총합 갱신하고 다음 조합 실행
"""
from sys import stdin
from itertools import combinations
from collections import deque

N = int(stdin.readline())
nodes = {i for i in range(1, N+1)}
people = [0, *map(int, stdin.readline().split())]
total_population = sum(people)
links = [set() for _ in range(N+1)]
for fr in range(1, N+1):
    for to in [*map(int, stdin.readline().split())][1:]:
        links[fr].add(to)
        links[to].add(fr)
answer = None
for num in range(1, N//2+1):
    for combination in combinations(nodes, num):
        comb_set = set(combination)
        remain_set = nodes - comb_set
        q = deque([comb_set.pop()])
        cnt = 0
        while q:
            node = q.popleft()
            cnt += people[node]
            for next_node in links[node]:
                if next_node in comb_set:
                    comb_set.remove(next_node)
                    q.append(next_node)
        if not comb_set:
            q = deque([remain_set.pop()] if remain_set else [])
            while q:
                node = q.popleft()
                for next_node in links[node]:
                    if next_node in remain_set:
                        remain_set.remove(next_node)
                        q.append(next_node)
            if not remain_set:
                if answer is None:
                    answer = abs(total_population-2*cnt)
                else:
                    answer = min(answer, abs(total_population-2*cnt))
print(answer if answer is not None else -1)
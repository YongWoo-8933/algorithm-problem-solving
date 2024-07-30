"""
백준 1516 게임 개발 (골드3)

1. 좀 특이한 위상정렬 문제로 일반적인 위상정렬을 진행하되, 
   완전탐색 진행시 특정한 조건을 만족하며 진행해야함.
2. inderees를 만드는것 까지는 똑같은데, 완전탐색 진행과정이 좀 다름
3. 4 건물을 만드는데 1과 3이 선행된다고 하자. 4, 1, 3이 각각 3분, 2분, 1분 만큼의 시간이 걸린다면,
   완전 탐색 진행시 1이 먼저 탐색될 경우 (1+3)분 / 3이 먼저 탐색될 경우 (2+3)분이 걸린다고 계산한다.
4. 두 경우 중 (1+3)분의 계산은 틀린 계산이다(1과 3을 동시에 짓기 시작할 경우 총 2분이 걸림)
5. 따라서 반드시 3이 먼저 실행되도록 보장해야만 한다.
6. 즉, 적은 시간이 걸리는 건물 노드가 먼저 탐색되도록 heapq를 사용해 풀면 된다.
"""
from sys import stdin
from heapq import heappop, heappush

input = stdin.readline
N = int(input())
next_building = [set() for _ in range(N+1)]
indegrees = [0]*(N+1)
times = [0]
for i in stdin:
    lst = [*map(int, i.split())]
    node = len(times)
    times.append(lst[0])
    for j in lst[1:-1]:
        next_building[j].add(node)
        indegrees[node] += 1
hq = []
for node in range(1, N+1):
    if indegrees[node]==0:
        heappush(hq, (times[node], node))
answer = [0]*(N+1)
while hq:
    time, node = heappop(hq)
    answer[node] += time
    for next_node in next_building[node]:
        indegrees[next_node] -= 1
        if indegrees[next_node]==0:
            heappush(hq, (time+times[next_node], next_node))
print(*answer[1:])
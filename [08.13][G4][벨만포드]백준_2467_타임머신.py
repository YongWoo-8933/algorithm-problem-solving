"""
백준 11657 타임머신 (골드 4)

1. 대표적인 벨만포드 알고리즘 문제
2. 벨만포드 알고리즘의 원리를 이해하고 있다면 풀 수 있음
"""
from sys import stdin

N, M = map(int, stdin.readline().split())
links = [[*map(int, i.split())] for i in stdin]
dists = [float("inf")]*(N+1)
dists[1] = 0
for i in range(N):
    for fr, to, time in links:
        if dists[to]>dists[fr]+time:
            dists[to] = dists[fr]+time
            if i == N-1:
                print(-1)
                exit()
answer = [i if i!=float("inf") else -1 for i in dists[2:]]
print(*answer)
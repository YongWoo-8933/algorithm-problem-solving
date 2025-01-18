"""
백준 5636 수문 (골드5)

1. BFS를 통한 완전 탐색(브루트포스)
2. 단, heapq를 써주면 쓸데없는 연산 줄일 수 있음
"""

from sys import stdin
from heapq import heappop, heappush

def main():
    N = int(stdin.readline())
    gates = [[*map(int, stdin.readline().split())] for _ in range(N)]
    for m in range(int(stdin.readline())):
        V, T = map(int, stdin.readline().split())
        hq = [(0, 0, -1)]
        while hq:
            cost, volume, idx = heappop(hq)
            if volume>=V:
                print(f"Case {m+1}: {cost}")
                break
            nidx = idx+1
            if nidx<N:
                heappush(hq, (cost, volume, nidx))
                heappush(hq, (cost+gates[nidx][1], volume+gates[nidx][0]*T, nidx))
        else:
            print(f"Case {m+1}: IMPOSSIBLE")

main()
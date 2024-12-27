"""
백준 1446 지름길 (실버1)

1. BFS 완전탐색
2. 다익스트라 풀이
"""
from sys import stdin
from collections import deque

def main():
    _, goal = map(int, stdin.readline().split())
    lst = []
    for i in stdin:
        fr, to, cost = map(int, i.split())
        if to<=goal and cost<to-fr:
            lst.append((fr, to, cost))
    N = len(lst)
    lst.sort()
    q = deque([(0, 0, 0)])
    answer = 0
    while q:
        idx, total, pos = q.popleft()
        if idx==N:
            answer = max(answer, total)
            continue
        fr, to, cost = lst[idx]
        q.append((idx+1, total, pos))
        if fr>=pos:
            q.append((idx+1, total+to-fr-cost, to))
    print(goal-answer)

main()
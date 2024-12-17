"""
백준 15655 N과M(실버3)

1. 연결관계 정리 후 BFS로 두 노드간 거리 계산

4 2
9 8 7 1
"""
from itertools import combinations

def main():
    _, M = map(int, input().split())
    lst = [*map(int, input().split())]
    lst.sort()
    for i in combinations(lst, M):
        print(*i)
main()

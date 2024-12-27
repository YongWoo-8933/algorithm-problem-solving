"""
백준 15655 N과M (실버3)

1. combinations 패키지로 모든 수열 출력
"""
from itertools import combinations


def main():
    _, M = map(int, input().split())
    lst = [*map(int, input().split())]
    lst.sort()
    for i in combinations(lst, M):
        print(*i)

        
main()

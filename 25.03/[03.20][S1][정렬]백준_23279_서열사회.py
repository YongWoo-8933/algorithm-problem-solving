"""
백준 23279 서열 사회 (실버1)

1. 정렬 후 조건에 맞게 번호 특정
"""
from sys import stdin

def main():
    N, K = map(int, input().split())
    for i in stdin:
        lst = [*map(int, i.split())]
        lst = [0]+sorted(lst[1:])
        answer = [0]
        for j in range(1, len(lst)):
            answer.append(answer[-1]+lst[j]-lst[j-1]+1)
        print(*answer[1:])

main()
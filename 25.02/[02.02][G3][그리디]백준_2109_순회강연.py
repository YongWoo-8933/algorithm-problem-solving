"""
백준 2109 순회강연 (골드3)

1. 다음 '과제' 문제와 완전히 똑같음.
"""
from sys import stdin
from heapq import heappush, heappop

def main():
    if not int(stdin.readline()):
        print(0)
        return
    works = [[*map(int, i.split())] for i in stdin]
    works.sort(key=lambda x: x[1])
    answer = 0
    hq = []
    day = works[-1][1]
    while day>0:
        while works and works[-1][1]==day:
            w, d = works.pop()
            heappush(hq, (-w, d))
        if hq:
            w, _ = heappop(hq)
            answer -= w
        day -= 1
    print(answer)

main()
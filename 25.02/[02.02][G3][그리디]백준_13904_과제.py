"""
백준 13904 과제 (골드3)

1. 날짜순으로 정렬해 마감일이 나중인 과제부터 접근
2. heap을 운영해 가장 점수가 높은 과제부터 제출하고, 나머지는 heap에 넣어둠
"""
from sys import stdin
from heapq import heappush, heappop

def main():
    stdin.readline()
    works = [[*map(int, i.split())] for i in stdin]
    works.sort()
    answer = 0
    hq = []
    day = works[-1][0]
    while day>0:
        while works and works[-1][0]==day:
            d, w = works.pop()
            heappush(hq, (-w, d))
        if hq:
            w, _ = heappop(hq)
            answer -= w
        day -= 1
    print(answer)

main()
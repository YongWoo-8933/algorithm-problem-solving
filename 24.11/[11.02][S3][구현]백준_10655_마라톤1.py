"""
백준 10655 마라톤1 (실버3)

1. 뺏을때 가장 거리가 큰 애를 빼주면됨
"""

from sys import stdin

def main():
    N = int(stdin.readline())
    lst = [[*map(int, i.split())] for i in stdin]
    total = 0
    max_v, min_v = 0, 0
    for i in range(1, N-1):
        x1, y1 = lst[i-1]
        x, y = lst[i]
        x2, y2 = lst[i+1]
        total += abs(x-x1)+abs(y-y1)
        max_dist = abs(x-x1)+abs(y-y1)+abs(x-x2)+abs(y-y2)
        min_dist = abs(y2-y1)+abs(x2-x1)
        if max_dist-min_dist>max_v-min_v:
            max_v, min_v = max_dist, min_dist
    print(total+abs(x-x2)+abs(y-y2)-max_v+min_v)

main()
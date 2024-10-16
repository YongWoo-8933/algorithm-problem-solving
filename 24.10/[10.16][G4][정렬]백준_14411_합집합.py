"""
백준 14411 합집합 (골드4)

1. x좌표 기준 정렬 후 y값 비교하며 순회하면 됨
"""

from sys import stdin

def main():
    stdin.readline()
    rectangles = [[0, 0]] + [[*map(int, i.split())] for i in stdin]
    rectangles.sort()
    answer = 0
    x, y = rectangles.pop()
    while rectangles:
        nx, ny = rectangles.pop()
        answer += (x-nx)*y
        x, y = nx, max(y, ny)
    print(answer)
main()
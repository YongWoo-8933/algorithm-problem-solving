"""
백준 8891 점숫자(실버4)

1. 수열합 공식으로 풀면 됨
"""
from sys import stdin

def dot_to_coord(n: int) -> tuple:
        i = int((-1+(1+8*n)**0.5)/2)
        s = i*(i+1)//2
        return (i, 1) if s==n else (n-s, i+2-n+s)

def coord_to_dot(x: int, y: int) -> int:
    n = (x+y)-2
    return n*(n+1)//2+x

def main():
    for _ in range(int(stdin.readline())):
        a, b = map(int, stdin.readline().split())
        ax, ay = dot_to_coord(a)
        bx, by = dot_to_coord(b)
        print(coord_to_dot(ax+bx, ay+by))

main()

"""
백준 31804 Chance! (골드4)

1. 도착점수에서 출발점수로 가는게 이득임(자연수 성질 활용)
2. BFS로 방문 체크하면서 이동동
"""
from sys import stdin
from math import log2

def main():
    for _ in range(int(stdin.readline())):
        n, a, b = map(int, stdin.readline().split())
        t = bin(min(a, b))[::-1].index('1')
        print(n-t)
        
main()
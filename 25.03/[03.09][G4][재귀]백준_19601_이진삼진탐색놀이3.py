"""
백준 19601 이진 삼진 탐색 놀이 3 (골드4)

1. 이진 탐색 횟수는 log 계산으로 바로 확인 가능
2. 삼진 탐색은 재귀로 돌리며 알아내면 됨
"""
from sys import stdin, setrecursionlimit
from math import log2

setrecursionlimit(10**5)

def main():

    def recur(n: int) -> int:
        if n==1: return 0
        elif n==2: return 1
        x = (n-1)//3
        return 2+recur(max(x, n-2*(x+1)))

    for _ in range(int(stdin.readline())):
        N = int(stdin.readline())
        print(f"{int(log2(N))} {recur(N)}")

main()
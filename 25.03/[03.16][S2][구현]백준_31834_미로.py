"""
백준 25318 solved.ac 2022 (실버1)

1. 경우를 나누어 하드코딩
"""
from sys import stdin

def main():
    for _ in range(int(stdin.readline())):
        N, S, E = map(int, stdin.readline().split())
        if S==E or abs(S-E)==N-1:
            print(0)
        elif abs(S-E)==1 or S in {1, N}:
            print(1)
        else:
            print(2)
            
main()
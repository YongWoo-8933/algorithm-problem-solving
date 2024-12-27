"""
백준 30704 정사각형 연결하기 (골드5)

1. 최대한 뭉치도록 계산
"""
from sys import stdin

def main():
    stdin.readline()
    for i in stdin:
        N = int(i)
        n = int(N**0.5)
        if N-n**2<1:
            print(4*n)
        elif N-n**2<n+1:
            print(4*n+2)
        else:
            print(4*n+4)

main()
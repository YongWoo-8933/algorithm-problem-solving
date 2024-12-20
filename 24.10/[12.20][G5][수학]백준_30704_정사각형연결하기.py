"""
백준 30704 정사각형 연결하기 (골드5)

1. combinations 패키지로 모든 수열 출력력
"""
from sys import stdin


def main():
    stdin.readline()
    for i in stdin:
        N = int(i)
        n = int(N**0.5)
        if N-n<=n:
            print(4*n+2)
        elif N-n<=2*n+1:
            print(4*n+4)
        elif N-n<=3*n+2:
            print(4*n+6)
        else:
            print(4*n+8)

        
main()

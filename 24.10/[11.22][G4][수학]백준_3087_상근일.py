"""
백준 3087 상근일(골드4)

1. 규칙을 찾아 수식을 찾으면 됨..
"""
from math import ceil

def main():
    N, K = map(int, input().split())
    if N<=K:
        print(2*N-1)
    else:
        answer = 2*K
        answer += ceil((N**2-K**2-K)/K)
        print(answer)
main()
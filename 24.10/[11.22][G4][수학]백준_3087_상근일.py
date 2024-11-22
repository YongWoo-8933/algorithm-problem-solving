"""
백준 3087 상근일(골드4)

1. 두더지가 나온 칸에 대해서는 최소공배수를 구하고
2. 나오지 않은 칸에 대해서는 배수가 아님을 체크하면됨
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
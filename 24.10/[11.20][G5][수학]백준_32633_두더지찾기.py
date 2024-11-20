"""
백준 32633 두더지 찾기(골드5)

1. 두더지가 나온 칸에 대해서는 최소공배수를 구하고
2. 나오지 않은 칸에 대해서는 배수가 아님을 체크하면됨
"""
from math import lcm

def main():
    N, L = map(int, input().split())
    A = [*map(int, input().split())]
    B = [*map(int, input().split())]
    X = 1
    for i in range(N):
        if B[i]==1:
            X = lcm(X, A[i])
        if X>L:
            print(-1)
            exit()
    if L<X:
        print(-1)
        exit()
    for i in range(N):
        if B[i]==0:
            if X%A[i]==0:
                print(-1)
                exit()
    print(X if X<=L else -1)

main()
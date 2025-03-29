"""
백준 15656 N과 M (7) (실버3)

1. 순열 구현방법대로 진행
"""

def main():
    N, M = map(int, input().split())
    lst = sorted(map(int, input().split()))
    def permutation(answer: str, size: int):
        if size==M:
            print(answer)
        elif size==0:
            for i in range(N):
                permutation(str(lst[i]), 1)
        else:
            for i in range(N):
                permutation(answer+f" {lst[i]}", size+1)

    permutation("", 0)

main()
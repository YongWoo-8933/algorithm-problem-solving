"""
백준 1309 동물원 (실버1)

1. 동물원을 한줄일때부터 쭉 dp로 계산하면됨
"""

def main():
    N = int(input())
    left, right, none = 1, 1, 1
    for _ in range(N-1):
        left, right, none = (right+none)%9901, (left+none)%9901, (left+right+none)%9901
    print((left+right+none)%9901)

main()

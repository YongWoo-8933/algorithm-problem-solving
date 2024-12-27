"""
백준 2785 체인 (실버1)

1. 정렬 후 몇개의 체인을 없앨 수 있는지 체크하면됨
"""

def main():
    N = int(input())
    chain_lengths = [*map(int, input().split())]
    chain_lengths.sort()
    remains = N-1
    for i in range(N):
        if chain_lengths[i]<=remains-1:
            remains -= chain_lengths[i]+1
        else:
            break
    print(N-1-i)

main()
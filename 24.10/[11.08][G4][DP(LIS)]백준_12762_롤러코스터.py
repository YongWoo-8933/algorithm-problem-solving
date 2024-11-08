"""
백준 12762 롤러코스터 (골드4)

1. 뺏을때 가장 거리가 큰 애를 빼주면됨
"""
from sys import stdin
from bisect import bisect_left

def main():
    N = int(stdin.readline())
    piles = [*map(int, stdin.readline().split())]
    answer = 1
    for lowest_pile_idx in range(N):
        lst1 = piles[lowest_pile_idx+1:]
        lst2 = piles[:lowest_pile_idx][::-1]
        cnt = -1
        for lst in [lst1, lst2]:
            LIS_lst = [piles[lowest_pile_idx]]
            for pile in lst:
                if pile>LIS_lst[-1]:
                    LIS_lst.append(pile)
                else:
                    LIS_lst[bisect_left(LIS_lst, pile)] = pile
            cnt += len(LIS_lst)
        answer = max(answer, cnt)
    print(answer)
main()


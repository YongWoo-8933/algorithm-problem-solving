"""
백준 12762 롤러코스터 (골드4)

1. LIS(Longest Increasing Subsequence) 응용문제
2. 어떤 기둥을 하이라이트의 최하단으로 둘지 정함
3. 최하단 기둥을 기준으로 기둥의 오른쪽 왼쪽 방향 각각에 대해 LIS 알고리즘 실행
4. LIS 길이를 통해 최장 하이라이트 구간 산출
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
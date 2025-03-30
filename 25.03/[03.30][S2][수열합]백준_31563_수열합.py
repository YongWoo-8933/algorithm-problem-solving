"""
백준 31563 수열 회전과 쿼리 (실버2)

1. 회전 = 시작 idx 변경으로 생각
2. 수열합을 활용해 합 구하기
"""
from sys import stdin

def main():
    N, _ = map(int, stdin.readline().split())
    lst = [*map(int, stdin.readline().split())]
    lst_sum = [0]
    for num in lst:
        lst_sum.append(lst_sum[-1]+num)
    idx = 0
    for i in stdin:
        option = [*map(int, i.split())]
        if option[0]==1:
            idx -= option[1]
            idx %= N
        elif option[0]==2:
            idx += option[1]
            idx %= N
        else:
            fr = (option[1]-1+idx)%N
            to = (option[2]-1+idx)%N
            if fr<=to:
                print(lst_sum[to+1]-lst_sum[fr])
            else:
                print(lst_sum[-1]-(lst_sum[fr]-lst_sum[to+1]))

main()
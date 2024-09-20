"""
백준 14718 용감한 용사 진수 (골드 4)

1. 완전 탐색 진행하면 됨
2. 힘, 민첩 스탯을 고정해놓고 지능 스택을 체크하며 이길수 있는 적의 수를 카운트
3. 정렬을 활용해 특정 임계점 이상부터는 연산을 줄임
"""
from sys import stdin

def main():
    N, K = map(int, stdin.readline().split())
    lst, str_lst, dex_lst = [], [], []
    for i in stdin:
        s, d, i = map(int, i.split())
        lst.append((s, d, i))
        str_lst.append(s)
        dex_lst.append(d)
    str_lst.sort()
    dex_lst.sort()
    lst.sort(key=lambda x: x[2])
    answer = float("inf")
    for str_stat in str_lst:
        for dex_stat in dex_lst:
            cnt = 0
            for s, d, i in lst:
                if str_stat+dex_stat+i>=answer:
                    break
                if str_stat>=s and dex_stat>=d:
                    cnt += 1
                if cnt>=K:
                    answer = min(answer, str_stat+dex_stat+i)
                    break
    print(answer)
main()
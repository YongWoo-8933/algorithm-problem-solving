"""
백준 1980 햄버거 사랑 (실버4)

1. 시간이 오래걸리는 버거 기준 0개 ~ 최대 개수까지 먹음
2. 각 케이스에서 먹을 수 있는 또다른 버거 수와 남은 시간으로 최대 경우 계산.
"""

def main():
    n, m, t = map(int, input().split())
    A, B = min(n, m), max(n, m)
    answer_cnt, answer_coke = 0, 10000
    for b in range(t//B+1):
        remain_coke = (t-B*b)%A
        burger_cnt = b+(t-B*b)//A
        if remain_coke<answer_coke:
            answer_cnt, answer_coke = burger_cnt, remain_coke
        elif remain_coke==answer_coke and burger_cnt>answer_cnt:
            answer_cnt = burger_cnt
    print(answer_cnt, answer_coke)

main()
"""
백준 2467 용액 (골드5)

1. 왼쪽 포인터(lp)와 오른쪽 포인터(rp) 설정
2. 각 포인터가 가리키는 용액의 혼합 특성값 산출
3. 혼합값이 음수면 lp를 증가, 양수면 rp를 감소시키며 최소 특성값 조합 찾기
"""

N = int(input())
values = [*map(int, input().split())]
lp, rp = 0, len(values)-1
min_mv, min_comb = float("inf"), (lp, rp)
while lp<rp:
    lv, rv, mv = values[lp], values[rp], values[lp]+values[rp]
    if abs(mv) < min_mv:
        min_mv, min_comb = abs(mv), (lp, rp)
    if mv<0:
        lp += 1
    else:
        rp -= 1
print(values[min_comb[0]], values[min_comb[1]])


    


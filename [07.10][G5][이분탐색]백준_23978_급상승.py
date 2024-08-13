"""
백준 23978 급상승 (골드5)

1. 적절한 가격 X를 이분탐색으로 찾아가면 됨
2. 날짜가 주어졌을때 총 얼마를 얻을 수 있는지 빠르게 연산하는
   로직을 구성하는게 포인트(O(n) 아래기만 하면 될 듯)
** 왠지 모르겠으나 python3으로 무조건 시간초과가 남 
   -> python 정답자가 없는 것으로 보아 테케 오류일듯
"""
def earn(k: int) -> int:
    global days, N
    coin_sum = N*k*(k+1)//2
    for i in range(N-1):
        diff = days[i+1]-days[i]
        if diff<k:
            dy = k-diff
            coin_sum -= dy*(dy+1)//2
    return coin_sum

N, K = map(int, input().split())
days = [*map(int, input().split())]
lp, rp = 1, 10**10
while lp<=rp:
    cp = (lp+rp)//2
    earned = earn(cp)
    if earned==K:
        print(cp)
        exit()
    elif earned>K:
        rp = cp-1
    else:
        lp = cp+1
print(rp if earn(rp)>=K else rp+1)




"""
백준 30804 과일 탕후루

1. 포인터 두개로 탕후루의 범위를 지정
2. 범위 내 과일의 종류가 2종류 이하면 범위를 늘리고 2종류보다 많으면 범위를 좁힘
3. 과정을 반복하며 종류가 2종류 이하일때 최장길이를 갱신
"""
N = int(input())
lst = [*map(int, input().split())]
lp, rp = 0, 0
category = [0]*10
answer = 0
while rp<N:
    category[lst[rp]] += 1
    while sum([0, 1][i!=0] for i in category)>2:
        category[lst[lp]] -= 1
        lp += 1
    rp += 1
    answer = max(answer, rp-lp)
print(answer)







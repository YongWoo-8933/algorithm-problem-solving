"""
백준 2110 공유기 설치 (골드4)
(* 어려워서 결국 해답 봄)
https://velog.io/@yoonuk/%EB%B0%B1%EC%A4%80-2110-%EA%B3%B5%EC%9C%A0%EA%B8%B0-%EC%84%A4%EC%B9%98-Python

1. 공유기 사이의 거리가 1일때, 2일때, 3일때.. 각각 최대 몇대의 공유기를 설치할 수 있는지 체크하는게 아이디어
2. 1을 생각해봤으나 거리가 최대 1,000,000,000까지 벌어질 수 있어 시간초과 우려로 포기함
3. 하지만 2에서 나타나는 한계를 이분탐색으로 해결하면 문제가 풀림
"""
from sys import stdin

N, C = map(int, stdin.readline().split())
houses = [int(i) for i in stdin]
houses.sort()
lp, rp = 1, houses[len(houses)-1]-houses[0]
while lp<=rp:
    cp = (lp+rp)//2
    cnt = 1
    cur_x = houses[0]
    for new_x in houses[1:]:
        if new_x>=cur_x+cp:
            cnt += 1
            cur_x = new_x
    if cnt<C:
        rp = cp-1
    else:
        lp = cp+1
print(rp)



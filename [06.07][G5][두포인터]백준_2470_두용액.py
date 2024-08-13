"""
백준 2470 두 용액

1. 두 포인터 풀이
2. 합의 최소 절대값을 업데이트하며 투포인터 알고리즘 진행
"""

N = int(input())
lst = sorted(map(int, input().split()))
answer, answer_set = 2*10**9, (0, N-1)
lp, rp= 0, N-1
while lp<rp:
    x = lst[lp]+lst[rp]
    if answer>abs(x):
        answer = abs(x)
        answer_set = (lst[lp], lst[rp])
    if x>0:
        rp -= 1
    elif x<0:
        lp += 1
    else:
        break
print(*answer_set)










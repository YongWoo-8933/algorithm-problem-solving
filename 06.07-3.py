"""
백준 2470 두 용액

1. 기본적으로 두 포인터 풀이
2. 왼쪽 포인터를 두고, 오른쪽 포인터를 합의 절대값이 가장 작아질때까지 왼쪽으로 이동
3. 해당 위치에서 오른쪽 포인터를 두고, 왼쪽 포인터만 한칸 오른쪽으로 이동
4. 위 과정을 반복하며 절대값합이 가장 작아지는 경우를 찾아 tuple 저장
"""

N = int(input())
lst = sorted(map(int, input().split()))
answer, answer_set = 2*10**9, (0, N-1)
lp, rp= 0, N-1
while lp<rp<N:
    while lp<rp-1 and abs(lst[lp]+lst[rp-1])<=abs(lst[lp]+lst[rp]):
        rp -= 1
    if abs(answer)>abs(lst[lp]+lst[rp]):
        answer = abs(lst[lp]+lst[rp])
        answer_set = (lst[lp], lst[rp])
    lp += 1
print(*answer_set)










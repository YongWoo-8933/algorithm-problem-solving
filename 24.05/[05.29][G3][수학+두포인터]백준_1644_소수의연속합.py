"""
백준 1644 소수의 연속합 (골드3)

1. 에라토스테네스의 체로 N이하 소수 모두 구하기
2. 산출된 소수 수열에 대해, 좌우 포인터(lp, rp)를 활용한 수열합으로 정답 카운트
"""
N = int(input())
prime = [True for _ in range(N+1)]
prime[1] = False
for i in range(4, N+1, 2):
    prime[i] = False
for i in range(3, int(N**0.5)+1, 2):
    if prime[i]:
        j = 3
        while i*j <= N:
            prime[i*j] = False
            j += 2
lst = [i for i in range(1, N+1) if prime[i]]
len_lst = len(lst)
lp, rp, S, answer = 0, 0, 0, 0
while lp<=rp:
    if S==N:
        answer += 1
        S -= lst[lp]
        lp += 1
    elif S>N:
        S -= lst[lp]
        lp += 1
    elif rp<len_lst:
        S += lst[rp]
        rp += 1
    else:
        break
print(answer)




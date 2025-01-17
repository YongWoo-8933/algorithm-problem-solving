"""
백준 13172 Σ

1. 페르마 소정리 활용
2. 분할거듭제곱으로 매우 큰 지수계산 실행
"""
from sys import stdin
from math import gcd, log2

def pow(x: int, n: int, MOD: int):
    for _ in range(n):
        x *= x
        x %= MOD
    return x

M = int(stdin.readline())
MOD = 1000000007
exponents = []
temp = MOD-2
while temp:
    exponent = int(log2(temp))
    exponents.append(exponent)
    temp -= 2**exponent
answer = 0
for i in stdin:
    N, S = map(int, i.split())
    inverse_N = 1
    if S % N:
        q = gcd(N, S)
        N, S = N//q, S//q
        for n in exponents:
            inverse_N *= pow(N, n, MOD)
            inverse_N %= MOD
    answer += ((S * inverse_N) % MOD)
    answer %= MOD
print(answer)
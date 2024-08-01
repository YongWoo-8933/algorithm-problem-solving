"""
백준 15668 방 번호 (골드4)

1. 두 자연수 A와 B중 작은값이 최대 몇까지 될 수 있는지 생각해보면 상한(limit)이 정해짐
2. 해당 상한까지 중복되는 경우를 제외하고 분할 가능 여부를 파악하면 됨
"""
from sys import stdin

def f(n: int, N: int):
    str_n = str(n)
    set_str_n = set(str_n)
    if len(str_n)!=len(set_str_n):
        return
    m = N-n
    str_m = str(m)
    for i in str_m:
        if i in set_str_n:
            break
    else:
        if len(str_m)==len(set(str_m)):
            print(str_n+" + "+str_m)
            exit()

N = int(stdin.readline())
limit = min(N//2, 87654)
for n in range(1, limit+1):
    f(n, N)
print(-1)
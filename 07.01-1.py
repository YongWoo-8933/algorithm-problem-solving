"""
백준 1011 Fly me to the Alpha Centauri (골드 5)

1. 수학적인 접근 필요(좌표차가 2^31까지 날 수 있어서 완전탐색 불가능)
2. 이동할 거리가 1~20 일때 정도만 직접 해보면 거리에 따른 제곱수 규칙을 찾을 수 있음
3. 이동할 거리가 몇의 제곱수사이에 있는지 찾고 적당한 로직을 추가해주면 됨
"""
from sys import stdin
from math import ceil

for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    x = b-a
    n = ceil(x**0.5)
    if x<=((n-1)**2+n**2)//2:
        print(2*n-2)
    else:
        print(2*n-1)
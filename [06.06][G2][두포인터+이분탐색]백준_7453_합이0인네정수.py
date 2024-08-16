"""
백준 7453 합이 0인 네 정수 (골드2)

* pypy3에서만 통과, python3에서는 더 시간복잡도를 줄일 방법을 찾아야함
1. A와 B의 모든 합을 dict 형식으로 저장(A[i]+B[j]=ab를 만족하는 ab가 몇개있는지 key-value로)
2. C와 D의 모든 원소합 C[i]+D[j]=cd라할때, -cd가 AB안에 몇개 존재하는지 셈
"""
from sys import stdin

N = int(input())
A, B, C, D = [], [], [], []
for i in stdin:
    a, b, c, d = map(int, i.split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
AB = {}
for a in A:
    for b in B:
        if a+b in AB:
            AB[a+b] += 1
        else:
            AB[a+b] = 1
answer = 0
for c in C:
    for d in D:
        x = -1*(c+d)
        if x in AB:
            answer += AB[x]
print(answer)







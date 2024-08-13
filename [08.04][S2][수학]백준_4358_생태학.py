"""
백준 4358 생태학 (실버2)

1. round의 사용법과 수의 소수점 자리수 표기에 유의해서 푼다.
"""
from sys import stdin

S = 0
d = {}
for name in stdin:
    name = name.strip()
    if name in d:
        d[name] += 1
    else:
        d[name] = 1
    S += 1
for name in sorted(d):
    print(f"{name} {round(100*d[name]/S, 4):.4f}")
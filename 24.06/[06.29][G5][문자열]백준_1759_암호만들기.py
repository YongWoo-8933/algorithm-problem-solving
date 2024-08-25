"""
백준 1759 암호 만들기(골드 5)

1. C개의 알파벳 중 L개의 알파벳을 골라 사전순으로 배열하면 끝
2. 여기서 모음 1개이상, 자음 2개이상 조건을 걸어 만족하는 애들만 출력
"""
from itertools import combinations

L, C = map(int, input().split())
chars = [*input().split()]
chars.sort()
aeiou = set("aeiou")
for comb in combinations(chars, L):
    comb_set = set(comb)
    subsection_set = comb_set-aeiou
    if 1<len(subsection_set)<len(comb_set):
        print("".join(sorted(comb)))


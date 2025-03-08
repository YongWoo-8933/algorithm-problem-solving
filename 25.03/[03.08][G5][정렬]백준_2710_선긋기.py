"""
백준 2710 선긋기 (골드5)

1. 선분 정렬 후 겹치는 선분부터 제거(set)
2. 왼쪽부터 순회하며 길이 계산
"""
from sys import stdin

def main():
    stdin.readline()
    lines = {tuple(map(int, i.split())) for i in stdin}
    lines = sorted(lines)
    answer = 0
    cur = -10**9
    for fr, to in lines:
        if to<=cur: continue
        answer += to-max(cur, fr)
        cur = to
    print(answer)

main()  
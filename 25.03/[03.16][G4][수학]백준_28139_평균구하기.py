"""
백준 28139 평균 구하기 (골드4)

1. 규칙을 찾고 수학 계산으로 풀이
"""
from sys import stdin

def main():
    N = int(stdin.readline())
    lst = [[*map(int, i.split())] for i in stdin]
    answer = 0
    for i in range(N):
        xi, yi = lst[i]
        for j in range(i+1, N):
            xj, yj = lst[j]
            answer += ((xi-xj)**2+(yi-yj)**2)**0.5
    print(answer*2/N)

main()
"""
백준 18248 제야의 종(실버2)

1. 앞사람일수록 들은 종소리가 많음. 따라서 들은 종소리 많은 순으로 정렬
2. 모든 종소리를 순회하며 앞사람이 못들은 종소리를 들은 뒷사람이 있다면 NO 출력
"""
from sys import stdin

def main():
    N, M = map(int, stdin.readline().split())
    lst = [[*map(int, i.split())] for i in stdin]
    lst.sort(key=lambda x: -sum(x))
    for i in range(M):
        zero_exist = False
        for j in range(N):
            if lst[j][i]==0:
                zero_exist = True
            elif zero_exist:
                print("NO")
                exit()
    print("YES")

main()

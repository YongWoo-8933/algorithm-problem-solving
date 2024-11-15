"""
백준 9753 짝 곱 (실버2)

1. 주어진 K값에서 1씩 더해가며 소인수가 4개인 수를 찾으면 됨
"""
from sys import stdin

def main():
    for _ in range(int(stdin.readline())):
        K = int(stdin.readline())
        while True:
            cnt = 0
            for i in range(2, int(K**0.5)+1):
                if K%i==0 and i!=K//i:
                    cnt += 1
                if cnt>1:
                    break
            if cnt==1:
                break
            K += 1
        print(K)

main()
"""
백준 5052 전화번호 목록 (골드4)

** 발상이 어렵지만 풀이는 생각보다 간단함..
1. 모든 전화번호를 정렬
2. 정렬하게되면 "123" "12340" 이런식으로 prefix가 겹치는 두 번호는 앞뒤로 붙게되어있음
3. 따라서 앞뒤 붙어있는 번호만 startswith라는 str 내장 메소드로 비교해주면 끝
"""
from sys import stdin

input = stdin.readline

def main():
    for _ in range(int(input())):
        n = int(input())
        lst = sorted(input().strip() for _ in range(n))
        for i in range(n-1):
            prefix, number = lst[i:i+2]
            if len(prefix)!=len(number) and number.startswith(prefix):
                print("NO")
                break
        else:
            print("YES")
    
main()
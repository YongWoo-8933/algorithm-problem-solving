"""
백준 17218 비밀번호 만들기 (골드4)

1. LCS알고리즘을 잘 숙지하고 있다면 그대로 실행하면 됨.
"""
from sys import stdin

def main():
    A, B = stdin.readline().strip(), stdin.readline().strip()
    lenA, lenB = len(A), len(B)
    dp = [[0]*(lenB+1) for _ in range(lenA+1)]
    for a in range(lenA):
        for b in range(lenB):
            dp[a+1][b+1] = dp[a][b]+1 if A[a]==B[b] else max(dp[a+1][b], dp[a][b+1])
    a, b = lenA, lenB
    reversed_answer = ""
    while dp[a][b]>0:
        if dp[a-1][b]==dp[a][b]:
            a -= 1
        elif dp[a][b-1]==dp[a][b]:
            b -= 1
        else:
            a -= 1
            b -= 1
            reversed_answer += A[a]
    print(reversed_answer[::-1])

main()
"""
백준 3359 사각사각 (실버1)

1. dp로 각 사각형이 세로로 놓일경우, 가로로 놓일 경우 최대 길이를 저장해놓고 쌓아나감.
"""

from sys import stdin

def main():
    stdin.readline()
    squares = [[*map(int, i.split())] for i in stdin]
    a, b = squares[0]
    py1, py2, dp1, dp2 = b, a, a, b
    for a, b in squares[1:]:
        dp1, dp2 = max(dp2+a+abs(b-py2), dp1+a+abs(b-py1)), max(dp2+b+abs(a-py2), dp1+b+abs(a-py1))
        py1, py2 = b, a
    print(max(dp1, dp2))

main()
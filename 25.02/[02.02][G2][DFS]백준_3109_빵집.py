"""
백준 3109 빵집 (골드2)

1. dfs로 이후 경로 성공 여부를 받고 결과에 따라 로직 분기처리
"""
from sys import stdin

def main():
    H, W = map(int, stdin.readline().split())
    MAP = [[*i.strip()] for i in stdin]
    answer = 0

    def dfs(row: int, col: int) -> bool:
        if col==W-1:
            return True
        ncol = col+1
        for nrow in [row-1, row, row+1]:
            if 0<=nrow<H and MAP[nrow][ncol]==".":
                MAP[nrow][ncol] = "x"
                if dfs(nrow, ncol):
                    return True
        return False

    for row in range(H):
        if dfs(row, 0):
            answer += 1
    print(answer)

main()
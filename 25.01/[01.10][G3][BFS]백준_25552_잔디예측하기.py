"""
백준 25552 잔디 예측하기 (골드3)

1. BFS로 움직일 수 있는 범위 전부 탐색하면 됨.
"""

from sys import stdin
from collections import deque

def main():
    H, W = map(int, stdin.readline().split())
    before = [stdin.readline().strip() for _ in range(H)]
    D = int(stdin.readline())
    after = [i.strip() for i in stdin]
    visited = [[False]*W for _ in range(H)]
    q = deque()
    for r in range(H):
        for c in range(W):
            if before[r][c]=="O":
                visited[r][c] = True
                q.append((r, c))
    while q:
        row, col = q.popleft()
        for dy in range(-D, D+1):
            for dx in range(-(D-abs(dy)), D-abs(dy)+1):
                nrow, ncol = row+dy, col+dx
                if 0<=nrow<H and 0<=ncol<W and not visited[nrow][ncol] and after[nrow][ncol]=="O":
                    visited[nrow][ncol] = True
                    q.append((nrow, ncol))
    for r in range(H):
        for c in range(W):
            if not visited[r][c] and after[r][c]=="O":
                print("NO")
                exit()
            elif visited[r][c] and after[r][c]=="X":
                print("NO")
                exit()
    print("YES")

main()
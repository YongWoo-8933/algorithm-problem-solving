"""
백준 1926 그림 (실버1)

1. BFS로 한바퀴 돌리면 됨
"""
from sys import stdin
from collections import deque

def main():
    H, W = map(int, stdin.readline().split())
    MAP = [[*map(int, i.split())] for i in stdin]
    cnt, area = 0, 0
    for row in range(H):
        for col in range(W):
            if MAP[row][col]==1:
                MAP[row][col] = 0
                cnt += 1
                temp = 1
                q = deque([(row, col)])
                while q:
                    r, c = q.popleft()
                    for nrow, ncol in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                        if 0<=nrow<H and 0<=ncol<W and MAP[nrow][ncol]==1:
                            MAP[nrow][ncol] = 0
                            temp += 1
                            q.append((nrow, ncol))
                area = max(area, temp)
    print(cnt, area)

main()

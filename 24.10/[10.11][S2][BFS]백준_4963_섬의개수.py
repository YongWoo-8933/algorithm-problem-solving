"""
백준 2468 안전영역 (실버1)

1. 모든 높이에 대해 BFS를 실시해 안전영역 카운트
"""
from sys import stdin
from collections import deque

def main():
    while True:
        W, H = map(int, stdin.readline().split())
        if not W and not H:
            break
        MAP = [[*map(int, stdin.readline().split())] for _ in range(H)]
        cnt = 0
        visited = [[False]*W for _ in range(H)]
        for row in range(H):
            for col in range(W):
                if MAP[row][col]==1 and not visited[row][col]:
                    visited[row][col] = True
                    cnt += 1
                    queue = deque([(row, col)])
                    while queue:
                        r, c = queue.popleft()
                        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                            if 0<=nr<H and 0<=nc<W and not visited[nr][nc] and MAP[nr][nc]==0:
                                visited[nr][nc] = True
                                queue.append((nr, nc))
        print(cnt)
main()
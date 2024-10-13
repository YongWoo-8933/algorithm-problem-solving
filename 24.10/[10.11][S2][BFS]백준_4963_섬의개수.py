"""
백준 4963 섬의 개수 (실버2)

1. 특정한 조건을 만족하는 BFS 실시
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
                        for nr, nc in [(r+1, c-1), (r+1, c), (r+1, c+1), (r-1, c-1), (r-1, c), (r-1, c+1), (r, c+1), (r, c-1)]:
                            if 0<=nr<H and 0<=nc<W and not visited[nr][nc] and MAP[nr][nc]==1:
                                visited[nr][nc] = True
                                queue.append((nr, nc))
        print(cnt)
main()
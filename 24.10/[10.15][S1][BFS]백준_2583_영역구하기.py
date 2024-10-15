"""
백준 2583 영역 구하기 (실버1)

1. BFS로 다 돌리면 끝
"""

from sys import stdin
from collections import deque

def main():
    H, W, K = map(int, stdin.readline().split())
    visited = [[False]*W for _ in range(H)]
    for i in stdin:
        x1, y1, x2, y2 = map(int, i.split())
        for y in range(y1, y2):
            for x in range(x1, x2):
                visited[y][x] = True
    answer = []
    for row in range(H):
        for col in range(W):
            if not visited[row][col]:
                visited[row][col] = True
                q = deque([(row, col)])
                area = 1
                while q:
                    r, c = q.popleft()
                    for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                        if 0<=nr<H and 0<=nc<W and not visited[nr][nc]:
                            visited[nr][nc] = True
                            area += 1
                            q.append((nr, nc))
                answer.append(area)
    print(len(answer), *sorted(answer))
main()
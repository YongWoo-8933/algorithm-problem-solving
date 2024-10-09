"""
백준 2468 안전영역 (실버1)

1. 모든 높이에 대해 BFS를 실시해 안전영역 카운트
"""
from sys import stdin
from collections import deque

def main():
    N = int(stdin.readline())
    MAP = [[*map(int, i.split())] for i in stdin]
    answer = 0
    for rain_height in range(min(min(i) for i in MAP)-1, max(max(i) for i in MAP)):
        visited = [[False]*N for _ in range(N)]
        cnt = 0
        for row in range(N):
            for col in range(N):
                if not visited[row][col] and MAP[row][col]>rain_height:
                    visited[row][col] = True
                    q = deque([(row, col)])
                    cnt += 1
                    while q:
                        r, c = q.popleft()
                        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                            if 0<=nr<N and 0<=nc<N and MAP[nr][nc]>rain_height and not visited[nr][nc]:
                                visited[nr][nc] = True
                                q.append((nr, nc))
        answer = max(answer, cnt)
    print(answer)
main()
"""
백준 1743 음식물 피하기 (실버1)

1. 간단한 bfs로 영역 크기 검사사
"""
from sys import stdin
from collections import deque

def main():
    H, W, _ = map(int, stdin.readline().split())
    MAP = [["."]*W for _ in range(H)]
    for i in stdin:
        r, c = map(int, i.split())
        MAP[r-1][c-1] = "#"
    answer = 0
    for row in range(H):
        for col in range(W):
            if MAP[row][col]=="#":
                MAP[row][col] = "."
                cnt = 1
                q = deque([(row, col)])
                while q:
                    r, c = q.popleft()
                    for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                        if 0<=nr<H and 0<=nc<W and MAP[nr][nc]=="#":
                            MAP[nr][nc] = "."
                            cnt += 1
                            q.append((nr, nc))
                answer = max(answer, cnt)
    print(answer)

main()
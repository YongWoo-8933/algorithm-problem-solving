"""
백준 24463 미로 (골드 4)

1. BFS를 진행하며 경로를 기억할 장치를 만드는게 포인트
2. 각 노드를 방문할 때, 어떤 노드로부터 왔는지 visited에 저장
3. 출구에 도착하면, visited에 저장되어있는 노드 경로를 따라 출구에서부터 경로 역추적
4. 과정에서 @값을 .으로 바꾸고, 입구에 다다르면 종료
"""
from sys import stdin
from collections import deque

def main():
    H, W = map(int, stdin.readline().split())
    MAP = [[*i.strip()] for i in stdin]
    s, e = None, None
    for row in range(H):
        for col in range(W):
            if MAP[row][col]==".":
                MAP[row][col] = "@"
                if row in (0, H-1) or col in (0, W-1):
                    if s is None:
                        s = (row, col)
                    elif e is None:
                        e = (row, col)
    visited = [[None]*W for _ in range(H)]
    visited[s[0]][s[1]] = (-1, -1)
    q = deque([s])
    while q:
        row, col = q.popleft()
        if (row, col)==e:
            break
        for nrow, ncol in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
            if 0<=nrow<H and 0<=ncol<W and visited[nrow][ncol] is None and MAP[nrow][ncol]=="@":
                visited[nrow][ncol] = (row, col)
                q.append((nrow, ncol))
    while (row, col) != (-1, -1):
        MAP[row][col] = "."
        row, col = visited[row][col]
    for i in range(H):
        print("".join(MAP[i]))
main()
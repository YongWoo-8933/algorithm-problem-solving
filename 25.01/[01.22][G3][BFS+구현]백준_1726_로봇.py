"""
백준 1726 로봇 (골드3)

1. BFS진행하되 각종 구현사항에 맞게 굴려야함..
2. heapq로 항상 최소 카운트부터 실행되도록 하고, 각 방향에 따라 방문체크
3. 1칸 2칸 3칸 전진하는 경우에 대한 처리가 중요
"""

from sys import stdin
from heapq import heappop, heappush

def main():
    H, W = map(int, stdin.readline().split())
    MAP = [[*map(int, stdin.readline().split())] for _ in range(H)]
    srow, scol, sdir = map(int, stdin.readline().split())
    erow, ecol, edir = map(int, stdin.readline().split())
    srow, scol, erow, ecol = srow-1, scol-1, erow-1, ecol-1
    dir_cnt = [
        [],
        [0, 1, 3, 2, 2],
        [0, 3, 1, 2, 2],
        [0, 2, 2, 1, 3],
        [0, 2, 2, 3, 1]
    ]
    d_rc = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[[False]*5 for __ in range(W)] for _ in range(H)]
    visited[srow][scol][sdir] = True
    hq = [(0, srow, scol, sdir)]
    answer = float('inf')
    while hq:
        cnt, row, col, cur_dir = heappop(hq)
        if cnt>=answer:
            break
        if row==erow and col==ecol:
            answer = min(answer, cnt+dir_cnt[cur_dir][edir]-1)
            continue
        for ndir in range(1, 5):
            dr, dc = d_rc[ndir]
            for dist in range(1, 4):
                nrow, ncol, ncnt = row+dr*dist, col+dc*dist, cnt+dir_cnt[cur_dir][ndir]
                if 0<=nrow<H and 0<=ncol<W:
                    if MAP[nrow][ncol]==1:
                        break
                    if not visited[nrow][ncol][ndir]:
                        visited[nrow][ncol][ndir] = True
                        heappush(hq, (ncnt, nrow, ncol, ndir))
    print(answer)

main()
"""
백준 2159 케익 배달 (골드3)

1. 이전 배달지에서 다음 배달지까지의 최단거리를 dp형식으로 저장해 계산
2. 각 배달지와 상하좌우 총 5개 지점에서 다음 5개 지점으로 25가지 경우를 모두 계산산
"""
from sys import stdin

def main():
    N = int(stdin.readline())
    sx, sy = map(int, stdin.readline().split())
    d = [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]
    lst = [[*map(int, i.split())] for i in stdin]
    dp = []
    fx, fy = lst[0]
    for dx, dy in d:
        nx, ny = fx+dx, fy+dy
        if 1<=nx and 1<=ny:
            dp.append(abs(nx-sx)+abs(ny-sy))
        else:
            dp.append(float("inf"))
    for i in range(1, N):
        sx, sy = lst[i-1]
        ex, ey = lst[i]
        new_dp = [float("inf")]*5
        for di in range(5):
            dsx, dsy = d[di]
            nsx, nsy = sx+dsx, sy+dsy
            if 1<=nsx and 1<=nsy:
                for dj in range(5):
                    dex, dey = d[dj]
                    nex, ney = ex+dex, ey+dey
                    if 1<=nex and 1<=ney and dp[di]+abs(nex-nsx)+abs(ney-nsy)<new_dp[dj]:
                        new_dp[dj] = dp[di]+abs(nex-nsx)+abs(ney-nsy)
        dp = new_dp
    print(min(dp))

main()
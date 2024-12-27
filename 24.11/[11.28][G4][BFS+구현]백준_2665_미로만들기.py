"""
백준 2665 미로만들기 (골드4)

1. heapq로 색을 바꾼 수가 적은 경우부터 BFS로 돌려 오른쪽 아래에 도달하면 종료
"""
from sys import stdin
from heapq import heappush, heappop

def main():
    N = int(stdin.readline())
    MAP = [i.strip() for i in stdin]
    visited = [[N*N]*N for _ in range(N)]
    hq = [(0, 0, 0)]
    while hq:
        cnt, row, col = heappop(hq)
        if row==N-1 and col==N-1:
            print(cnt)
            exit()
        for nrow, ncol in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
            if 0<=nrow<N and 0<=ncol<N:
                ncnt = cnt
                if MAP[nrow][ncol]=="0":
                    ncnt += 1
                if ncnt<visited[nrow][ncol]:
                    visited[nrow][ncol] = ncnt
                    heappush(hq, (ncnt, nrow, ncol))
        
main()
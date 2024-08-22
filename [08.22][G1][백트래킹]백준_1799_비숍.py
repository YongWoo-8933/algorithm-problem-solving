"""
백준 1799 비숍 (골드 1)

1. 백트래킹에서 검은/흰칸 구분을 더해 구현해야함.
2. 대각선 인덱싱에 유의하여 검은칸 백트래킹 + 흰칸 백트래킹 한번씩 진행
"""
from sys import stdin, setrecursionlimit

def main():
    setrecursionlimit(10**6)
    N = int(stdin.readline())
    board = [[*map(int, i.split())] for i in stdin]
    diag = [False]*(2*N-1)

    def backtracking(cnt: int, idx: int) -> int:
        if idx>2*N-2:
            return cnt
        temp = backtracking(cnt, idx+2)
        row = min(idx, N-1)
        while row>=0:
            col = idx-row
            if 0<=col<N and board[row][col]==1 and diag[N-1+row-col]==False:
                diag[N-1+row-col] = True
                temp = max(temp, backtracking(cnt+1, idx+2))
                diag[N-1+row-col] = False
            row -= 1
        return temp
    
    answer = backtracking(0, 0)
    print(backtracking(answer, 1))

main()
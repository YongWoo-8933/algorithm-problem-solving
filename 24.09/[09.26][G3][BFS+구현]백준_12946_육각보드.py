"""
백준 12946 육각 보드 (골드 3)

*** 완전 탐색 진행할때는 '필요없어보여도' 방문체크 반드시 하기... ***

1. 보드를 순회하며 X를 만나면 BFS 진행
2. 각 BFS에서 주변 6개의 칸을 확인
3. 1만 있으면 2 색칠 / 2만 있으면 1 색칠 / 1, 2모두 있으면 3 반환후 종료(색은 최대 3개까지 가능)
"""
from sys import stdin
from collections import deque

def main():
    N = int(stdin.readline())
    board = [[*i.strip()] for i in stdin]
    answer = 0
    visited = [[False]*N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if board[row][col]=="X" and not visited[row][col]:
                q = deque([(row, col)])
                visited[row][col] = True
                while q:
                    row, col = q.popleft()
                    one_exist, two_exist = False, False
                    for nrow, ncol in [(row-1, col), (row-1, col+1), (row, col-1), (row, col+1), (row+1, col-1), (row+1, col)]:
                        if 0<=nrow<N and 0<=ncol<N:
                            if board[nrow][ncol]==1:
                                one_exist = True
                            elif board[nrow][ncol]==2:
                                two_exist = True
                            elif board[nrow][ncol]=="X" and not visited[nrow][ncol]:
                                visited[nrow][ncol] = True
                                q.append((nrow, ncol))
                    if one_exist and two_exist:
                        print(3)
                        exit()
                    elif one_exist:
                        board[row][col] = 2
                        answer = max(answer, 2)
                    else:
                        board[row][col] = 1
                        answer = max(answer, 1)
    print(answer)
main()
"""
백준 1525 퍼즐 (골드2)

1. BFS로 0 자리를 움직이며 나올 수 있는 모든 퍼즐의 모양을 탐색하면 됨
2. 효율적인 메모리 활용을 위해 퍼즐 모양을 1차원(string)으로 풀어 저장
3. 몇번째 움직였는지, 0의 위치, 퍼즐의 모양을 전달하며 각 퍼즐모양의
   0의 위치로부터 row, col을 가져와 이동시키는 등의 연산을 진행 
"""
from sys import stdin
from collections import deque

def main():
    board = "".join(stdin.readline().strip().split())
    board += "".join(stdin.readline().strip().split())
    board += "".join(stdin.readline().strip().split())
    completed = "123456780"
    visited = {board}
    q = deque([(0, board.find("0"), board)])
    while q:
        cnt, zero_idx, board = q.popleft()
        if board==completed:
            print(cnt)
            exit()
        row, col = zero_idx//3, zero_idx%3
        for nrow, ncol in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
            if 0<=nrow<3 and 0<=ncol<3:
                new_zero_idx = nrow*3+ncol
                board_lst = list(board)
                board_lst[zero_idx], board_lst[new_zero_idx] = board_lst[new_zero_idx], board_lst[zero_idx] 
                new_board = "".join(board_lst)
                if new_board not in visited:
                    visited.add(new_board)
                    q.append((cnt+1, new_zero_idx, new_board))
    print(-1)

main()
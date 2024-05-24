"""
백준 2239 스도쿠

1. 백트래킹 알고리즘 구현
2. 행, 열, 칸 숫자의 중복을 피하기 위해 각각 set을 만들어둠
3. 0번째 ~ 80번째 칸까지 idx부여, 각 칸에대한 back_tracking 함수 실행
4. 각 실행에서는 해당 칸이 비어있을 경우(0인경우) 숫자 1~9에대한 back_tracking 실행
5. idx가 80보다 커지면 정답 배열을 출력하고 exit을 통해 초과 출력 방지
"""
board = [[0]*9 for _ in range(9)]
row_check = [set() for _ in range(9)]
col_check = [set() for _ in range(9)]
block_check = [set() for _ in range(9)]

for i in range(9):
    s = input()
    for j in range(9):
        x = int(s[j])
        board[i][j] = x
        row_check[i].add(x)
        col_check[j].add(x)
        block_check[(i//3)*3+j//3].add(x)

def back_tracking(board: list, row_check: list, col_check: list, block_check: list, idx: int):
    if idx>80:
        print(*["".join(str(j) for j in i) for i in board])
        exit()
    else:
        row, col, block = idx//9, idx%9, (idx//27)*3+(idx%9)//3
        if board[row][col]:
            back_tracking(board, row_check, col_check, block_check, idx+1)
        else:
            for number in range(1, 10):
                if number not in row_check[row] and \
                   number not in col_check[col] and \
                   number not in block_check[block]:
                    board[row][col] = number
                    row_check[row].add(number)
                    col_check[col].add(number)
                    block_check[block].add(number)
                    back_tracking(board, row_check, col_check, block_check, idx+1)
                    board[row][col] = 0
                    row_check[row].remove(number)
                    col_check[col].remove(number)
                    block_check[block].remove(number)

back_tracking(board, row_check, col_check, block_check, 0)


    


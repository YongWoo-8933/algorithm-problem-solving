"""
코드트리 - 바이러스 실험
https://www.codetree.ai/training-field/frequent-problems/problems/virus-experiment/submissions?page=3&pageSize=20

1. 배지의 영양상태를 표시하는 board list와 바이러스의 위치, 
   age를 표시하는 virus list를 운영
2. 지시에 맞게 k번 시행
3. 시간을 줄이기 위해 eat부분에서 나이가 5의 배수가 된 바이러스의 좌표를
   list에 담아놓고 return값으로 반환함
4. 반환받은 바이러스 list를 통해 바이러스 번식 진행
"""
from sys import stdin

# 1, 2번 과정
def eat() -> list:
    global n, board, virus
    age_5_virus = []
    for row in range(n):
        for col in range(n):
            if virus[row][col]:
                n_lst = []
                foods = 0
                for age in sorted(virus[row][col]):
                    if board[row][col]>=age:
                        board[row][col] -= age
                        n_lst.append(age+1)
                        if (age+1)%5==0:
                            age_5_virus.append((row, col))
                    else:
                        foods += age//2
                board[row][col] += foods
                virus[row][col] = n_lst
    return age_5_virus

# 3번 과정
def reproduce(age_5_virus: list):
    global n, d, virus
    for row, col in age_5_virus:
        for dx, dy in d:
            nrow, ncol = row+dy, col+dx
            if 0<=nrow<n and 0<=ncol<n:
                virus[nrow][ncol].append(1)

n, m, k = map(int, stdin.readline().split())
add_food = [[*map(int, stdin.readline().split())] for _ in range(n)]
virus = [[[] for _ in range(n)] for __ in range(n)]
for i in stdin:
    r, c, a = map(int, i.split())
    virus[r-1][c-1].append(a)
board = [[5]*n for _ in range(n)]
d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for _ in range(k):
    age_5_virus = eat()
    reproduce(age_5_virus)
    # 4 과정
    for row in range(n):
        for col in range(n):
            board[row][col] += add_food[row][col]

answer = 0
for row in range(n):
    for col in range(n):
        answer += len(virus[row][col])

print(answer)



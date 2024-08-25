"""
백준 17406 배열 돌리기 4 (골드 4)

1. 순열 모듈 사용해서 나올 수 있는 모든 command 회전 순서 구하기
2. 모든 회전을 하드코딩하고, 배열값의 최소 찾기
"""
from sys import stdin
from itertools import permutations
from copy import deepcopy

def rotate(arr: list, row: int, col: int, diff: int) -> list:
    for d in range(1, diff+1):
        temp = arr[row-d][col-d]
        for c in range(col-d+1, col+d+1):
            arr[row-d][c], temp = temp, arr[row-d][c]
        for r in range(row-d+1, row+d+1):
            arr[r][col+d], temp = temp, arr[r][col+d]
        for c in range(col+d-1, col-d-1, -1):
            arr[row+d][c], temp = temp, arr[row+d][c]
        for r in range(row+d-1, row-d-1, -1):
            arr[r][col-d], temp = temp, arr[r][col-d]
    return arr

def main():
    H, _, K = map(int, stdin.readline().split())
    arr = [[*map(int, stdin.readline().split())] for _ in range(H)]
    origin_commands = [[*map(int, i.split())] for i in stdin]
    answer = 5000
    for commands in permutations(origin_commands, K):
        temp_arr = deepcopy(arr)
        for row, col, diff in commands:
            temp_arr = rotate(temp_arr, row-1, col-1, diff)
        answer = min(answer, min(sum(temp_arr[i]) for i in range(H)))
    print(answer)

main()
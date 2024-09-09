"""
백준 14719 빗물 (골드5)

1. 각 행의 왼쪽 끝, 오른쪽 끝 벽 여부를 확인하고
2. 그 사이 빈칸을 모두 더함
"""
from sys import stdin

def main():
    H, W = map(int, stdin.readline().split())
    ground = [[1]*W for _ in range(H)]
    lst = [*map(int, stdin.readline().split())]
    for col in range(W):
        for row in range(H-1, H-1-lst[col], -1):
            ground[row][col] = 0
    answer = 0
    for row in range(H-1, -1, -1):
        fr = None
        for col in range(W):
            if ground[row][col]==0:
                fr = col
                break
        if fr is None:
            break
        to = None
        for col in range(W-1, -1, -1):
            if ground[row][col]==0:
                to = col
                break
        answer += sum(ground[row][fr:to+1])
    print(answer)

main()
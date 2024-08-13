"""
백준 21610 마법사 상어와 비바라기 (골드 5)

1. 평범한 시뮬레이션 문제
2. 구름 이동 시 각 끝부분이 연결되도록 N으로 나눈 나머지 값으로 설정
3. 구름이 사라진 칸에 새 구름이 생기지 않도록 기억해두기(cloud_map 운영)
"""
from sys import stdin

def sol():
    N, _ = map(int, stdin.readline().split())
    diff = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    board = [[*map(int, stdin.readline().split())] for _ in range(N)]
    cloud = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
    for i in stdin:
        d, s = map(int, i.split())
        cloud_map = [[False]*N for _ in range(N)]
        # 모든 구름 이동 + 비 내림
        for i in range(len(cloud)):
            row, col = cloud[i]
            dy, dx = diff[d]
            cloud[i] = (row+dy*s)%N, (col+dx*s)%N
            row, col = cloud[i]
            cloud_map[row][col] = True
            board[row][col] += 1
        # 물복사 버그
        for row, col in cloud:
            cnt = 0
            for drow, dcol in [(row-1, col-1), (row+1, col+1), (row-1, col+1), (row+1, col-1)]:
                if 0<=drow<N and 0<=dcol<N and board[drow][dcol]:
                    cnt += 1
            board[row][col] += cnt
        # 새 구름 생성
        new_cloud = []
        for row in range(N):
            for col in range(N):
                if board[row][col]>=2 and not cloud_map[row][col]:
                    board[row][col] -= 2
                    new_cloud.append([row, col])
        cloud = new_cloud
    print(sum(sum(i) for i in board))

sol()



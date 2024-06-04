"""
백준 25682 체스판 다시 칠하기 2

1. 수열합과 비슷하게 dp table을 작성
2. dp의 i행 j열은 ixj크기의 보드판에서 색을 다시 칠해야할 칸의 갯수를 의미함
3. 따라서 i행 j열의 값은 (i-1행 j열값 + i행 j-1열값 - i-1행 j-1열값)이 되어 dp풀이 가능
4. dp table이 완성되면 K*K보드판에서 찾을 수 있는 가장 작은 변경값을 산출
5. 4의 과정에서 역시 dp의 (i행 j열값 - i행 j-K열값 - i-K행 j열값 + i-K행 j-K열값)이 K*K판 위에서의 변경값임을 이용
"""
from sys import stdin

def make_dp_table(board: list) -> list:
    global H, W
    # 왼쪽 위가 B인 dp table 생성
    # margin을 두기 위해 보드보다 크게 설정
    dp = [[0]*(W+1) for _ in range(H+1)]
    for row in range(H):
        for col in range(W):
            dp[row+1][col+1] = dp[row][col+1]+dp[row+1][col]-dp[row][col]+[0, 1]["BW"[(row%2+col%2)%2]!=board[row][col]]
    return dp

def find_min_change(dp: list) -> int:
    global H, W, K
    answer = 2000*2000
    # K*K판중 가장 변경횟수가 적은것 찾기
    for row in range(K, H+1):
        for col in range(K, W+1):
            x = dp[row][col]-dp[row-K][col]-dp[row][col-K]+dp[row-K][col-K]
            answer = min(answer, x, K*K-x)
    return answer

H, W, K = map(int, stdin.readline().split())
board = [i.strip() for i in stdin]
dp = make_dp_table(board)
print(find_min_change(dp))





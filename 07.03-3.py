"""
백준 1520 내리막 길 (골드3)
** BFS로 풀고 시간초과
** 백준 dp 태그 힌트보고 dp+dfs로 풀고 성공

1. 방문했던 노드를 다시 방문할 수 있으므로 같은 경로를 탐색해 시간 초과됨
   ex) 1 > 2 > 3 > 4 > 5 > 6 ...
       1 > 7 > 8 > 4 > 5 > 6 ...
       위와 같은 경로라면 4 이후 경로는 두번 계산되는 셈
2. 위 예에서, 방문했던 첫 번째 순환에서 4이후 경로에 대해 저장해놓았다면,
   두 번째 순환은 4이후 경로를 계산하지 않아도 된다.
3. 각 순환이 목적지에 도달할 수 있는지 알아야 하므로 BFS+DP 불가, DFS+DP 선정
4. DP는 H행 W열의 크기로 만들며 각 원소는 [None, None, None, None]으로 초기화
5. 원소의 각 값은 해당 칸에서 상/하/좌/우에 있는 칸으로 갈 경우 목적지에
   도달하는 경우의 수를 저장하기로 한다.
6. DFS는 row행 col열에서 다음을 수행
   - row==H-1, col==W-1일 경우 (목적지라면) 1을 return
   - 목적지가 아니라면 result = 0으로 두고 상/하/좌/우 칸에대해 다음 수행
   - dp[row][col]에 해당 방향의 결과가 있으면 그 값을 result에 추가
   - dp[row][col]에 해당 방향의 결과가 없으면(None일 경우) 재귀를 통해 얻어내 갱신
   - 네 방향에 대한 순회가 끝나면 더해진 result값을 return
"""
from sys import stdin, setrecursionlimit

def dfs(row, col) -> int:
    global board, dp, H, W
    if row==H-1 and col==W-1:
        return 1
    result = 0
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(4):
        dy, dx = d[i]
        nrow, ncol = row+dy, col+dx
        if 0<=nrow<H and 0<=ncol<W and board[nrow][ncol]<board[row][col]:
            if dp[row][col][i] is None:
                dp[row][col][i] = dfs(nrow, ncol)
            result += dp[row][col][i]
    return result

setrecursionlimit(10**6)
H, W = map(int, stdin.readline().split())
board = [[*map(int, i.split())] for i in stdin]
dp = [[[None, None, None, None] for _ in range(W)] for __ in range(H)]
print(dfs(0, 0))
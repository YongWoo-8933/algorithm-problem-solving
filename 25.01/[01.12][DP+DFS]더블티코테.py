"""
더블티 코테 (난이도 골드 2~4 예상)

1. 기본적으로 DFS 순회
2. 방문 여부를 체크. 이때 새로운 금화를 먹었다면 저장
3. 해당 금화수를 먹고 노드를 방문한 적이 있다면, 남은 시간을 기준으로 체크
4. 금화수도, 남은시간도 적다면 패스

test

4 8
#.#O
.O#.
.#SO
O...

3
"""

from sys import stdin

def main():
    N, T = map(int, stdin.readline().split())
    MAP = [[*i] for i in stdin]
    for srow in range(N):
        for scol in range(N):
            if MAP[srow][scol]=="S":
                break
        else:
            continue
        break
    # 먹은금화수 : 남은시간
    visited = [[dict() for __ in range(N)] for _ in range(N)]
    visited[srow][scol][0] = T

    def dfs(movable: int, golds: int, row: int, col: int):
        if not movable:
            return
        for nrow, ncol in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
            if 0<=nrow<N and 0<=ncol<N and MAP[nrow][ncol]!="#":
                if MAP[nrow][ncol]=="O":
                    MAP[nrow][ncol] = "."
                    if golds+1 not in visited[nrow][ncol]:
                        visited[nrow][ncol][golds+1] = movable-1
                        dfs(movable-1, golds+1, nrow, ncol)
                    elif movable-1>=visited[nrow][ncol][golds+1]:
                        visited[nrow][ncol][golds+1] = movable-1
                        dfs(movable-1, golds+1, nrow, ncol)
                    MAP[nrow][ncol] = "O"
                else:
                    if golds not in visited[nrow][ncol]:
                        visited[nrow][ncol][golds] = movable-1
                        dfs(movable-1, golds, nrow, ncol)
                    elif movable-1>=visited[nrow][ncol][golds]:
                        visited[nrow][ncol][golds] = movable-1
                        dfs(movable-1, golds, nrow, ncol)

    dfs(T, 0, srow, scol)
    answer = 0
    for row in range(N):
        for col in range(N):
            if visited[row][col]:
                answer = max(answer, max(visited[row][col]))
    print(answer)

main()
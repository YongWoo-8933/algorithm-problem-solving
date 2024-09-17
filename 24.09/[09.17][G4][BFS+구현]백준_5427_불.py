"""
백준 5427 불 (골드 4)

첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스는 최대 100개이다.

각 테스트 케이스의 첫째 줄에는 빌딩 지도의 너비와 높이 w와 h가 주어진다. (1 ≤ w,h ≤ 1000)

다음 h개 줄에는 w개의 문자, 빌딩의 지도가 주어진다.

'.': 빈 공간
'#': 벽
'@': 상근이의 시작 위치
'*': 불
각 지도에 @의 개수는 하나이다.

출력
각 테스트 케이스마다 빌딩을 탈출하는데 가장 빠른 시간을 출력한다. 
빌딩을 탈출할 수 없는 경우에는 "IMPOSSIBLE"을 출력한다.

예제 입력 1 
5
4 3
####
#*@.
####
7 6
###.###
#*#.#*#
#.....#
#.....#
#..@..#
#######
7 4
###.###
#....*#
#@....#
.######
5 5
.....
.***.
.*@*.
.***.
.....
3 3
###
#@#
###
예제 출력 1 
2
5
IMPOSSIBLE
IMPOSSIBLE
IMPOSSIBLE
"""
from sys import stdin
from collections import deque

def main():
    for _ in range(int(stdin.readline())):
        W, H = map(int, stdin.readline().split())
        MAP = []
        q = deque()
        pos_row, pos_col = 0, 0
        for row in range(H):
            MAP.append([*stdin.readline().strip()])
            for col in range(W):
                if MAP[-1][col]=="*":
                    q.append((0, 0, row, col))
                elif MAP[-1][col]=="@":
                    pos_row, pos_col = row, col
        q.append((1, 0, pos_row, pos_col))
        sanguen_cnt = 1
        escaped = False
        while q:
            id, cnt, row, col = q.popleft()
            # 불일 경우
            if id==0:
                for nrow, ncol in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                    if 0<=nrow<H and 0<=ncol<W and MAP[nrow][ncol] in "@.":
                        MAP[nrow][ncol] = "*"
                        q.append((id, cnt+1, nrow, ncol))
                for i in range(H):
                    print(*MAP[i])
            # 상근이일 경우
            elif id==1:
                sanguen_cnt -= 1
                for nrow, ncol in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                    if 0<=nrow<H and 0<=ncol<W:
                        if MAP[nrow][ncol]==".":
                            sanguen_cnt += 1
                            MAP[nrow][ncol] = "@"
                            q.append((id, cnt+1, nrow, ncol))
                    else:
                        escaped = True
                        break
                else:
                    if sanguen_cnt:
                        for i in range(H):
                            print(*MAP[i])
                        continue
                break
        if escaped:
            print(cnt+1)
        else:
            print("IMPOSSIBLE")

main()
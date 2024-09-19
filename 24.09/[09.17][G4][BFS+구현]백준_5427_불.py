"""
백준 5427 불 (골드 4)

1. 불부터 q에 집어넣고 마지막에 상근이의 위치를 q에 집어넣음
2. 이대로 BFS를 돌리면 반드시 불부터 이동함이 보장됨
3. q에 불 이동 명령만 남아있다면 반복문 종료
4. 상근이가 다음턴에 밖으로 나갈 수 있으면 반복문 종료
"""
from sys import stdin
from collections import deque

def main():
    for _ in range(int(stdin.readline())):
        W, H = map(int, stdin.readline().split())
        MAP = [[*stdin.readline().strip()] for _ in range(H)]
        q = deque()
        for row in range(H):
            for col in range(W):
                if MAP[row][col]=="*":
                    q.append((0, 0, row, col))
        for row in range(H):
            for col in range(W):
                if MAP[row][col]=="@":
                    q.append((1, 0, row, col))
                    break
            else:
                continue
            break
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
                        continue
                break
        if escaped:
            print(cnt+1)
        else:
            print("IMPOSSIBLE")

main()
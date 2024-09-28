"""
백준 11559 Puyo Puyo (골드 4)

1. 평범한 BFS문제로, 조건에 맞게 구현을 곁들이면 됨.
2. 순회하다가 색깔을 만나면 주변으로 BFS 전개
3. 4개 이상이라면 터뜨리기
4. 터뜨린 행위가 없었다면 break,
5. 있었다면 색을 아래로 미는 작업 실행
"""
from sys import stdin
from collections import deque

def main():
    MAP = [[*i.strip()] for i in stdin]
    answer = 0
    while True:
        boom_exist = False
        visited = [[False]*6 for _ in range(12)]
        for row in range(12):
            for col in range(6):
                if MAP[row][col]!="." and not visited[row][col]:
                    visited[row][col] = True
                    q = deque([(row, col)])
                    temp = []
                    while q:
                        r, c = q.popleft()
                        temp.append((r, c))
                        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                            if 0<=nr<12 and 0<=nc<6 and not visited[nr][nc] and MAP[nr][nc]==MAP[row][col]:
                                visited[nr][nc] = True
                                q.append((nr, nc))
                    if len(temp)>=4:
                        boom_exist = True
                        for r, c in temp:
                            MAP[r][c] = "."
        if not boom_exist:
            break
        else:
            answer += 1
            new_MAP = [["."]*6 for _ in range(12)]
            for col in range(6):
                row_idx = 11
                for row in range(11, -1, -1):
                    if MAP[row][col]!=".":
                        new_MAP[row_idx][col] = MAP[row][col]
                        row_idx -= 1
            MAP = new_MAP
    print(answer)
main()
"""
백준 11559 Puyo Puyo (골드 4)

뿌요뿌요의 룰은 다음과 같다.
필드에 여러 가지 색깔의 뿌요를 놓는다. 뿌요는 중력의 영향을 받아 아래에 바닥이나 
다른 뿌요가 나올 때까지 아래로 떨어진다.

뿌요를 놓고 난 후, 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 
연결된 같은 색 뿌요들이 한꺼번에 없어진다. 이때 1연쇄가 시작된다.

뿌요들이 없어지고 나서 위에 다른 뿌요들이 있다면, 역시 중력의 영향을 받아 
차례대로 아래로 떨어지게 된다.

아래로 떨어지고 나서 다시 같은 색의 뿌요들이 4개 이상 모이게 되면 또 터지게 되는데, 
터진 후 뿌요들이 내려오고 다시 터짐을 반복할 때마다 1연쇄씩 늘어난다.

터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고 
여러 그룹이 터지더라도 한번의 연쇄가 추가된다.

남규는 최근 뿌요뿌요 게임에 푹 빠졌다. 이 게임은 1:1로 붙는 대전게임이라 잘 쌓는 것도 중요하지만, 
상대방이 터뜨린다면 연쇄가 몇 번이 될지 바로 파악할 수 있는 능력도 필요하다. 
하지만 아직 실력이 부족하여 남규는 자기 필드에만 신경 쓰기 바쁘다. 
상대방의 필드가 주어졌을 때, 연쇄가 몇 번 연속으로 일어날지 계산하여 남규를 도와주자!

입력
총 12개의 줄에 필드의 정보가 주어지며, 각 줄에는 6개의 문자가 있다.

이때 .은 빈공간이고 .이 아닌것은 각각의 색깔의 뿌요를 나타낸다.

R은 빨강, G는 초록, B는 파랑, P는 보라, Y는 노랑이다.

입력으로 주어지는 필드는 뿌요들이 전부 아래로 떨어진 뒤의 상태이다. 
즉, 뿌요 아래에 빈 칸이 있는 경우는 없다.

출력
현재 주어진 상황에서 몇연쇄가 되는지 출력한다. 하나도 터지지 않는다면 0을 출력한다.

예제 입력 1 
......
......
......
......
......
......
......
......
.Y....
.YG...
RRYG..
RRYGG.
예제 출력 1 
3
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
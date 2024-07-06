"""
백준 14891 톱니바퀴 (골드5)

1. 기어를 번호에 맞는 인덱스 자리에 저장해놓음
2. 돌릴 기어와 방향이 주어지면, 해당 기어를 중심으로 BFS실행
3. 왼쪽 기어의 3시 톱니와 자신의 9시 톱니의 극이 다른경우와
   오른쪽 기어의 9시 톱니와 자신의 3시 톱니의 극이 다른경우 해당 기어를 돌림
4. 돌릴때는 deque 모듈의 rotate 메소드를 활용하면 쉬움(+면 시계방향, -면 반시계방향)
5. 명령을 모두 수행하면 기어의 상태에따라 점수를 리턴
"""
from sys import stdin
from collections import deque

gears = [deque()]
for _ in range(4):
    gears.append(deque(map(int, stdin.readline().strip())))
stdin.readline()
for i in stdin:
    g, r = map(int, i.split())
    visited = [0]*5
    visited[g] = 1
    rotate_gears = []
    q = deque([(g, r)])
    while q:
        g, r = q.popleft()
        rotate_gears.append((g, r))
        if 1<=g+1<5 and not visited[g+1] and gears[g][2]!=gears[g+1][6]:
            visited[g+1] = 1
            q.append((g+1, -1 if r>0 else 1))
        if 1<=g-1<5 and not visited[g-1] and gears[g][6]!=gears[g-1][2]:
            visited[g-1] = 1
            q.append((g-1, -1 if r>0 else 1))
    for g, r in rotate_gears:
        gears[g].rotate(r)
print(gears[1][0]+2*gears[2][0]+4*gears[3][0]+8*gears[4][0])
















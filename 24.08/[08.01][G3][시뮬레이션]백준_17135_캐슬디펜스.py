"""
백준 17135 캐슬 디펜스 (골드3)

1. 조건에 맞게 시뮬레이션 하드코딩하면 됨
2. combinations로 아처가 있을 수 있는 column 조합을 모두 진행
3. 각 아처 위치조합에 따라 보드와 맞힌 적군 수를 초기화
4. BFS 방식으로 사거리에따른 적군 탐색 진행
   (deque으로 queue를 만들어 순서에 유의하면, 같은 사거리 내에서는 반드시
   가장 왼쪽에 있는 칸부터 탐색하게 되어있음)
5. ** 같은 적군이 여러개의 화살을 맞을 수 있으므로 모든 아처가 화살을 쏘고 나서
      맞은 적군을 보드에 정산
"""
from sys import stdin
from itertools import combinations
from collections import deque
from copy import deepcopy

H, W, D = map(int, stdin.readline().split())
MAP = [[*map(int, i.split())] for i in stdin]
answer = 0
for archers in combinations(range(W), 3):
    temp_map = deque(deepcopy(MAP))
    temp_answer = 0
    while any(1 in i for i in temp_map):
        hit = set()
        # 아처 화살 쏘기
        for col in archers:
            q = deque([(1, H-1, col)])
            visited = {(H-1, col)}
            while q:
                dist, row, col = q.popleft()
                if temp_map[row][col]==1:
                    hit.add((row, col))
                    break
                if dist<D:
                    for nrow, ncol in [(row, col-1), (row-1, col), (row, col+1)]:
                        if 0<=nrow<H and 0<=ncol<W and (nrow, ncol) not in visited:
                            visited.add((nrow, ncol))
                            q.append((dist+1, nrow, ncol))
        # 맞은 적군 정산
        temp_answer += len(hit)
        for row, col in hit:
            temp_map[row][col] = 0
        # 적군 전진
        temp_map.pop()
        temp_map.appendleft([0]*W)
    answer = max(answer, temp_answer)
print(answer)
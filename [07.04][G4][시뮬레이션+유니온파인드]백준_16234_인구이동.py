"""
백준 16234 인구 이동 (골드4)

1. 일자에 따른 단순 구현에서 union-find 개념이 추가된 형태
2. 인구 차이를 비교하며 경계를 없앨 수 있으면 union 시킴
3. 없앨 경계가 하나도 없으면 해당 일자를 print하고 break
4. 없앨 경계가 있을 경우 우선 root 정보를 저장한 table을 정리
5. 각 연합의 가입 국가수와 총 국민수를 저장
6. 모든 칸에대해 새로 바뀐 인구 정보를 갱신
"""
from sys import stdin

def find(x: int) -> int:
    global parents
    if parents[x]!=x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a: int, b: int):
    global parents
    ra, rb = find(a), find(b)
    if ra!=rb:
        parents[max(ra, rb)] = min(ra, rb)

N, L, R = map(int, stdin.readline().split())
MAP = [[*map(int, i.split())] for i in stdin]
for day in range(2001):
    openable = False
    parents = [i for i in range(N**2+1)]
    for row in range(N):
        for col in range(row%2, N, 2):
            p_n = MAP[row][col]
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nrow, ncol = row+dy, col+dx
                if 0<=nrow<N and 0<=ncol<N and L<=abs(MAP[nrow][ncol]-p_n)<=R:
                    union(row*N+col, nrow*N+ncol)
                    openable = True
    if not openable:
        print(day)
        break
    for i in range(1, N**2+1):
        parents[i] = find(i)

    union_dict = {}
    for row in range(N):
        for col in range(N):
            root = parents[row*N+col]
            if root in union_dict:
                union_dict[root][0] += 1
                union_dict[root][1] += MAP[row][col]
            else:
                union_dict[root] = [1, MAP[row][col]]
    for row in range(N):
        for col in range(N):
            cnt, value = union_dict[parents[row*N+col]]
            MAP[row][col] = value//cnt
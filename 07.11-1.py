"""
백준 1976 여행 가자 (골드4)

1. 여행지와 여행지 사이에 이동할 수 있는 경로가 존재하기만 하면 됨.
2. 따라서 경로들을 union-find로 묶었을 때 서로 다른 집합에 속한
   여행지가 있다면 불가능한 경로가 된다.
3. union find로 경로가 이어진 여행지들을 묶은 후,
4. 마지막 경로에서 root 체크를 했을때 root가 2개 이상이면 NO,
   root가 끝까지 한개만 있다면 YES를 출력
"""
from sys import stdin

def find(x: int) -> int:
    global parents
    if x!=parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(a: int, b: int):
    global parents
    ra, rb = find(a), find(b)
    if ra!=rb:
        parents[max(ra, rb)] = min(ra, rb)

N, M = int(stdin.readline()), int(stdin.readline())
parents = [i for i in range(N+1)]
for fr in range(1, N+1):
    temp = [0, *map(int, stdin.readline().split())]
    for to in range(1, N+1):
        if temp[to]:
            union(fr, to)
for i in range(1, N+1):
    parents[i] = find(i)
roots = set()
for i in map(int, stdin.readline().split()):
    roots.add(parents[i])
    if len(roots)>1:
        print("NO")
        exit()
print("YES")
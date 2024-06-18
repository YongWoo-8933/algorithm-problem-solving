"""
백준 2162 선분 그룹

** ccw알고리즘, union-find알고리즘 공부 반드시 필요함
1. ccw를 통해 두 선분의 교차를 판단
2. 각 선분을 돌며 union-find 알고리즘을 통해 교차하는 선분끼리 그룹지어줌
3. 마지막에 parent의 root를 한번 갱신해준 후 그룹수와 최대 그룹원수를 산출
"""

from sys import stdin

def ccw(x1, y1, x2, y2, x3, y3) -> int:
    return  x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3

def is_cross(x1, y1, x2, y2, x3, y3, x4, y4) -> bool:
    ccw1, ccw2 = ccw(x1, y1, x2, y2, x3, y3), ccw(x1, y1, x2, y2, x4, y4)
    ccw3, ccw4 = ccw(x3, y3, x4, y4, x1, y1), ccw(x3, y3, x4, y4, x2, y2)

    if ccw1*ccw2==0 and ccw3*ccw4==0:
        if x1==x2:
            # 수직 선분
            if min(y1, y2)>max(y3, y4) or min(y3, y4)>max(y1, y2):
                return False
            else:
                return True
        else:
            # 그 외 선분
            if min(x1, x2)>max(x3, x4) or min(x3, x4)>max(x1, x2):
                return False
            else:
                return True
    elif ccw1*ccw2==0:
        return ccw3*ccw4<0
    elif ccw3*ccw4==0:
        return ccw1*ccw2<0
    else:
        return ccw3*ccw4<0 and ccw1*ccw2<0

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

N = int(input())
lines = [[*map(int, i.split())] for i in stdin]
parents = [*range(N)]
for i in range(N):
    x1, y1, x2, y2 = lines[i]
    for j in range(i+1, N):
        x3, y3, x4, y4 = lines[j]
        if is_cross(x1, y1, x2, y2, x3, y3, x4, y4):
            union(i, j)
parents = [find(i) for i in range(N)]
print(sum(1 for i in range(N) if i==parents[i]))
print(max(parents.count(i) for i in range(N)))




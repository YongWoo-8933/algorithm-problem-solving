"""
프로그래머스 - 아이템 줍기
https://school.programmers.co.kr/learn/courses/30/lessons/87694
"""
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    coords = [[0]*102 for _ in range(102)]
    rectangle = [*map(lambda x: [2*i for i in x], rectangle)]
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1, x2+1):
            ys = range(y1, y2+1) if x in [x1, x2] else [y1, y2]
            for y in ys:
                for r in rectangle:
                    if r[0]<x<r[2] and r[1]<y<r[3]:
                        break
                else:
                    coords[x][y] = 1
                    
    visited = [[0]*102 for _ in range(102)]
    visited[characterX][characterY] = 1
    q = deque([(0, characterX, characterY)])
    while q:
        cnt, x, y = q.popleft()
        if x==itemX and y==itemY:
            return cnt//2
        cnt += 1
        for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            nx, ny = x+dx, y+dy
            if coords[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((cnt, nx, ny))
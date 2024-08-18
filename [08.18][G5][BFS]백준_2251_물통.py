"""
백준 2251 물통 (골드5)

1. 조건에 맞게 BFS 구현, 각 물통에 남은 물의 양을 기준으로 방문했던 조합인지 체크
2. 모든 경우를 탐색하는 것이므로 굳이 q일 필요가 없음. stack이 좀더 빠름
"""
from sys import stdin

def main():
    limits = [*map(int, stdin.readline().split())]
    fr_to = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
    visited = {(0, 0, limits[2])}
    stack = [[0, 0, limits[2]]]
    answer = set()
    while stack:
        v = stack.pop()
        if v[0]==0:
            answer.add(v[2])
        for (fr, to) in fr_to:
            newv = v.copy() 
            if newv[fr]!=0 and newv[to]<limits[to]:
                move = min(newv[fr], limits[to]-newv[to])
                newv[fr], newv[to] = newv[fr]-move, newv[to]+move
                newv_set = tuple(newv)
                if newv_set not in visited:
                    visited.add(newv_set)
                    stack.append(newv)
    print(*sorted(answer))

main()
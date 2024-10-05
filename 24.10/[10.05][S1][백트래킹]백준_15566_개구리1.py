"""
백준 15566 개구리 1 (실버1)

1. 세세한 조건에 맞게 백트래킹 진행해주면 됨
2. positions는 개구리 번호에 따라 배정된 연꽃의 번호를 저장
3. frogs는 연꽃 번호에 따라 배정된 개구리의 번호를 저장
4. 첫번째 개구리부터 차례대로 idx를 증가시키며 연꽃에 배정
5. 각 back tracking 로직에서 먼저 해당 연꽃이 비었나 확인
6. 연꽃이 비어있다면, 인접한 연꽃에 개구리가 있는지 확인, 없다면 패스
7. 개구리가 있다면 대화의 흥미도가 같은지 확인
"""
from sys import stdin

def main():
    N, _ = map(int, stdin.readline().split())
    interest = [[]] + [[0, *map(int, stdin.readline().split())] for _ in range(N)]
    prefer_position = [set()] + [{*map(int, stdin.readline().split())} for _ in range(N)]
    links = [set() for _ in range(N+1)]
    for i in stdin:
        fr, to, category = map(int, i.split())
        links[fr].add((to, category))
        links[to].add((fr, category))
    positions = [0]*(N+1)
    frogs = [0]*(N+1)

    def back_tracking(idx: int):
        if idx==N+1:
            print("YES")
            print(*frogs[1:])
            exit()
        for pos in prefer_position[idx]:
            if frogs[pos]==0:
                is_valid = True
                for linked_pos, category in links[pos]:
                    if frogs[linked_pos]==0:
                        pass
                    elif interest[idx][category]!=interest[frogs[linked_pos]][category]:
                        is_valid = False
                if is_valid:
                    positions[idx] = pos
                    frogs[pos] = idx
                    back_tracking(idx+1)
                    positions[idx] = 0
                    frogs[pos] = 0
    
    back_tracking(1)
    print("NO")

main()
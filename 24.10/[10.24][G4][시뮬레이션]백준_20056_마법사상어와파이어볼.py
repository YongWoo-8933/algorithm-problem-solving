"""
백준 20056 마법사 상어와 파이어볼 (골드4)

** 시뮬레이션, 별다른 아이디어없이 구현만 하면 됨 **
** class를 통한 구현을 해봄. 가독성은 좋지만 debuging에서 썩 좋지 않아보임 **
** 성능은 두 풀이 모두 큰 차이 없음(미세하게 class가 느림) **
"""

from sys import stdin

class Fireball:
    def __init__(self, mass: int, direction: int, velocity: int):
        self.mass = mass
        self.direction = direction
        self.velocity = velocity

def main1():
    N, _, K = map(int, stdin.readline().split())
    d_yx = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    MAP = [[[] for _ in range(N)] for __ in range(N)]
    for i in stdin:
        r, c, m, s, d = map(int, i.split())
        MAP[r-1][c-1].append(Fireball(m, d, s))
    for _ in range(K):
        new_MAP = [[[] for _ in range(N)] for __ in range(N)]
        # 이동
        for row in range(N):
            for col in range(N):
                for fireball in MAP[row][col]:
                    dy, dx = d_yx[fireball.direction]
                    nrow, ncol = row+dy*fireball.velocity, col+dx*fireball.velocity
                    nrow, ncol = nrow%N, ncol%N
                    new_MAP[nrow][ncol].append(fireball)
        # 병합/분리
        for row in range(N):
            for col in range(N):
                cnt = len(new_MAP[row][col])
                if cnt<=1:
                    continue
                mass_sum, velocity_sum = 0, 0
                is_all_even, is_all_odd = True, True
                for fireball in new_MAP[row][col]:
                    mass_sum += fireball.mass
                    velocity_sum += fireball.velocity
                    if fireball.direction%2==0:
                        is_all_odd = False
                    else:
                        is_all_even = False
                new_fireballs = []
                if mass_sum//5>0:
                    if is_all_odd or is_all_even:
                        start_direction = 0
                    else:
                        start_direction = 1
                    for new_direction in range(start_direction, 8, 2):
                        new_fireballs.append(Fireball(mass_sum//5, new_direction, velocity_sum//cnt))
                new_MAP[row][col] = new_fireballs
        MAP = new_MAP
    answer = 0
    for row in range(N):
        for col in range(N):
            for fireball in MAP[row][col]:
                answer += fireball.mass
    print(answer)

def main2():
    N, _, K = map(int, stdin.readline().split())
    d_yx = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    MAP = [[[] for _ in range(N)] for __ in range(N)]
    for i in stdin:
        r, c, m, s, d = map(int, i.split())
        MAP[r-1][c-1].append([m, s, d])
    for _ in range(K):
        new_MAP = [[[] for _ in range(N)] for __ in range(N)]
        # 이동
        for row in range(N):
            for col in range(N):
                for fireball in MAP[row][col]:
                    dy, dx = d_yx[fireball[2]]
                    nrow, ncol = row+dy*fireball[1], col+dx*fireball[1]
                    nrow, ncol = nrow%N, ncol%N
                    new_MAP[nrow][ncol].append(fireball)
        # 병합/분리
        for row in range(N):
            for col in range(N):
                cnt = len(new_MAP[row][col])
                if cnt<=1:
                    continue
                mass_sum, velocity_sum = 0, 0
                is_all_even, is_all_odd = True, True
                for fireball in new_MAP[row][col]:
                    mass_sum += fireball[0]
                    velocity_sum += fireball[1]
                    if fireball[2]%2==0:
                        is_all_odd = False
                    else:
                        is_all_even = False
                new_fireballs = []
                if mass_sum//5>0:
                    if is_all_odd or is_all_even:
                        start_direction = 0
                    else:
                        start_direction = 1
                    for new_direction in range(start_direction, 8, 2):
                        new_fireballs.append([mass_sum//5, velocity_sum//cnt, new_direction])
                new_MAP[row][col] = new_fireballs
        MAP = new_MAP
    answer = 0
    for row in range(N):
        for col in range(N):
            for fireball in MAP[row][col]:
                answer += fireball[0]
    print(answer)

main2()
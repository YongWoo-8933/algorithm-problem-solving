"""
백준 15684 사다리 조작 (골드3)

** 극악의 백트래킹 문제 **
"""

from sys import stdin

# cnt: 현재까지 생성한 가로선의 수
# limit: 최대 생성 가능한 가로선의 수
def back_tracking(cnt: int, limit: int):
    global ladder, answer, H, N

    # 현재 limit에서 이미 답이 나옴
    if answer!=-1:
        return
    
    # 현재 사다리 상태에서 몇개의 인덱스가 맞는지 확인
    cur_mateched = check()

    # limit-cnt: 앞으로 생성 가능한 가로선의 수
    # (limit-cnt)*2: 앞으로 변경 가능한 인덱스의 수
    # cur_mateched + (limit-cnt)*2: 앞으로 조작을 통해 맞출 수 있는 인덱스의 최대값
    if cur_mateched+(limit-cnt)*2 < N:
        return
    
    # 더이상 그을 수 있는 가로선이 없으면 종료
    if cnt==limit:
        if cnt==N:
            answer = cnt
        return
    
    # 그을 수 있는 가로선이 있다면 백트래킹 진행
    for h in range(1, H+1):
        for i in range(1, N):
            if ladder[h][i]==0 and ladder[h][i+1]==0:
                ladder[h][i], ladder[h][i+1] = i+1, i
                back_tracking(cnt+1, limit)
                ladder[h][i], ladder[h][i+1] = 0, 0

# 현재 사다리 상태에서 몇개의 인덱스가 맞는지 return
# ex) 1 2 3 4 5    
#     2 1 4 3 5    => 1 return
def check() -> int:
    global ladder, N, H
    matched = 0
    for i in range(1, N+1):
        cur_i = i
        for h in range(1, H+1):
            if ladder[h][cur_i]!=0:
                cur_i = ladder[h][cur_i]
        if cur_i==i:
            matched += 1
    return matched

# ladder => 사다리 모양에 맞게 상태 저장
# ex) 3행 2열 - 3행 3열 이어져있다면
#     3행 2열값 = 3
#     3행 3열값 = 2
#     이어져있지 않다면 0
N, M, H = map(int, stdin.readline().split())
ladder = [[0]*(N+1) for _ in range(H+1)]
for i in stdin:
    a, b = map(int, i.split())
    ladder[a][b] = b+1
    ladder[a][b+1] = b
answer = -1
# limit: 최대 가로선 생성 횟수
# limit를 0 > 1 > 2 > 3 으로 늘리며 백트래킹 진행
for limit in range(4):
    back_tracking(0, limit)
    if answer != -1:
        break
print(answer)
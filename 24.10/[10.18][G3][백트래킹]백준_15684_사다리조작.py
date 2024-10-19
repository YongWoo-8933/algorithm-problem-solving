"""
백준 15684 사다리 조작 (골드3)

** 극악의 백트래킹 문제 **
"""

from sys import stdin

def back_tracking(cnt: int, limit: int):
    global ladder, answer, H, N

    if answer!=-1:
        return
    
    cur_mateched = check()
    if cur_mateched+(limit-cnt)*2 < N:
        return
    
    if cnt==limit:
        if cnt==N:
            answer = cnt
        return
    
    for h in range(1, H+1):
        for i in range(1, N):
            if ladder[h][i]==0 and ladder[h][i+1]==0:
                ladder[h][i], ladder[h][i+1] = i+1, i
                back_tracking(cnt+1, limit)
                ladder[h][i], ladder[h][i+1] = 0, 0

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

N, M, H = map(int, stdin.readline().split())
ladder = [[0]*(N+1) for _ in range(H+1)]
for i in stdin:
    a, b = map(int, i.split())
    ladder[a][b] = b+1
    ladder[a][b+1] = b
answer = -1
for limit in range(4):
    back_tracking(0, limit)
    if answer != -1:
        break
print(answer)
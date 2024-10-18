"""
백준 15684 사다리 조작 (골드3)

1. x좌표 기준 정렬 후 y값 비교하며 순회하면 됨
"""

from sys import stdin

def back_tracking(cnt: int, h: int, i: int, is_checked: bool) -> bool:
    global ladder, answer, H, N
    if cnt>=answer:
        return False
    elif h==H and i==N:
        return False
    elif i==N:
        return back_tracking(cnt, h+1, 1, is_checked)
    else:
        if not is_checked and check():
            answer = cnt
            return True
        if back_tracking(cnt, h, i+1, True):
            return True
        if ladder[h][i]==0 and ladder[h][i+1]==0:
            ladder[h][i] = i+1
            ladder[h][i+1] = i
            result2 = back_tracking(cnt+1, h, i+1, False)
            ladder[h][i] = 0
            ladder[h][i+1] = 0
            return result2
        return False

def check() -> bool:
    global ladder, N, H
    for i in range(1, N+1):
        cur_i = i
        for h in range(1, H+1):
            if ladder[h][cur_i]!=0:
                cur_i = ladder[h][cur_i]
        if cur_i!=i:
            return False
    return True

N, M, H = map(int, stdin.readline().split())
ladder = [[0]*(N+1) for _ in range(H+1)]
for i in stdin:
    a, b = map(int, i.split())
    ladder[a][b] = b+1
    ladder[a][b+1] = b
answer = H*N
if back_tracking(0, 1, 1, False):
    print(answer)
else:
    print(-1)
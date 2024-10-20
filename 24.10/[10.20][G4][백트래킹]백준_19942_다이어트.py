"""
백준 19942 다이어트 (골드4)

1. 침착하게 백트래킹으로 진행하면됨
"""

from sys import stdin

def backtracking(idx: int):
    global p, f, s, v, mp, mf, ms, mv, cost, answer, lst, answer_lst
    if cost>answer:
        return
    if idx==N:
        if p>=mp and f>=mf and s>=ms and v>=mv:
            answer = cost
            answer_lst.append(cur_lst.copy())
        return
    backtracking(idx+1)
    p, f, s, v, cost = p+lst[idx][0], f+lst[idx][1], s+lst[idx][2], v+lst[idx][3], cost+lst[idx][4]
    cur_lst.append(idx+1)
    backtracking(idx+1)
    p, f, s, v, cost = p-lst[idx][0], f-lst[idx][1], s-lst[idx][2], v-lst[idx][3], cost-lst[idx][4]
    cur_lst.remove(idx+1)

N = int(stdin.readline())
mp, mf, ms, mv = map(int, stdin.readline().split())
lst = [[*map(int, i.split())] for i in stdin]
max_cost = sum(lst[i][4] for i in range(N))+1
answer = max_cost
answer_lst = []
p, f, s, v, cost, cur_lst = 0, 0, 0, 0, 0, []
backtracking(0)
answer_lst.sort()
if answer==max_cost:
    print(-1)
else:
    print(answer)
    print(*answer_lst[0])
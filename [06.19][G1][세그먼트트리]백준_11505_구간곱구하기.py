"""
백준 11505 구간 곱 구하기 (골드1)
1. 06.19-1 구간 합 구하기와 거의 똑같음
2. 합과달리 곱해서 0이되지 않도록 조심
"""
from sys import stdin, setrecursionlimit
from math import log2, ceil

def segment(idx: int, fr: int, to: int) -> int:
    global lst, segment_tree
    if fr==to:
        segment_tree[idx] = lst[fr]
    else:
        c = (fr+to)//2
        segment_tree[idx] = (segment(2*idx, fr, c)*segment(2*idx+1, c+1, to))%1000000007
    return segment_tree[idx]

def edit(idx: int, target: int, change_to: int, fr: int, to: int) -> int:
    global segment_tree
    if target<fr or target>to:
        pass
    elif fr==to==target:
        segment_tree[idx] = change_to
    else:
        c = (fr+to)//2
        segment_tree[idx] = (edit(2*idx, target, change_to, fr, c)*edit(2*idx+1, target, change_to, c+1, to))%1000000007
    return segment_tree[idx]

def get_value(idx: int, target_fr: int, target_to: int, fr: int, to: int) -> int:
    global segment_tree
    if target_to<fr or target_fr>to:
        return 1
    elif fr>=target_fr and to<=target_to:
        return segment_tree[idx]
    else:
        c = (fr+to)//2
        return (get_value(2*idx, target_fr, target_to, fr, c)*get_value(2*idx+1, target_fr, target_to, c+1, to))%1000000007
        
setrecursionlimit(10**6)
N, M, K = map(int, stdin.readline().split())
lst = [int(stdin.readline()) for _ in range(N)]
segment_tree = [0]*(1+2**(ceil(log2(N))+1))
segment(1, 0, N-1)
for i in stdin:
    a, b, c = map(int, i.split())
    if a==1:
        edit(1, b-1, c, 0, N-1)
    else:
        print(get_value(1, b-1, c-1, 0, N-1))

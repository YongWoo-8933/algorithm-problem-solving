"""
백준 2357 최솟값과 최댓값 (골드1)

1. 세그먼트 트리 알고리즘 공부 후 구현하면됨
2. 일반적인 수열합 세그먼트 트리가 아닌 최대, 최소값 트리를 구현
"""
from sys import stdin, setrecursionlimit
from math import log2, ceil

def segment(idx: int, fr: int, to: int) -> list:
    global segment_tree, lst
    if fr==to:
        segment_tree[idx] = [lst[fr], lst[fr]]
        return segment_tree[idx]
    c = (fr+to)//2
    left, right = segment(2*idx, fr, c), segment(2*idx+1, c+1, to)
    segment_tree[idx] = [min(left[0], right[0]), max(left[1], right[1])]
    return segment_tree[idx]

def f(idx: int, target_fr: int, target_to: int, node_fr: int, node_to) -> int:
    global segment_tree
    if node_to<target_fr or target_to<node_fr:
        return [1000000001, 0]
    elif node_fr>=target_fr and node_to<=target_to:
        return segment_tree[idx]
    c = (node_fr+node_to)//2
    left, right = f(2*idx, target_fr, target_to, node_fr, c), f(2*idx+1, target_fr, target_to, c+1, node_to)
    return [min(left[0], right[0]), max(left[1], right[1])]

setrecursionlimit(10**6)
N, _ = map(int, stdin.readline().split())
lst = [int(stdin.readline()) for _ in range(N)]    
segment_tree = [[0, 0] for _ in range(1+2**(ceil(log2(N))+1))]
segment(1, 0, N-1)
for i in stdin:
    fr, to = map(int, i.split())
    print(*f(1, fr-1, to-1, 0, N-1))


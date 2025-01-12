"""
백준 31989 기숙사 택배물 배달 (골드5)

1. 택배 보관소를 기준으로 좌우 시뮬레이션 돌리면 됨.
"""

from sys import stdin

def main():
    N, _ = map(int, stdin.readline().split())
    dists = [0, *map(int, stdin.readline().split())]
    items = [[] for _ in range(2*N+2)]
    weight_sum_1, weight_sum_2 = 0, 0
    for i in stdin:
        idx, weight = map(int, i.split())
        items[idx].append(weight)
        if idx<N+1:
            weight_sum_1 += weight
        elif idx>N+1:
            weight_sum_2 += weight
    answer = 0 
    if weight_sum_1:
        for node in range(N, 0, -1):
            answer += (dists[node+1]-dists[node])*(weight_sum_1+1)
            weight_sum_1 -= sum(items[node])
            if not weight_sum_1:
                break
        answer += dists[N+1]-dists[node]
    if weight_sum_2:
        for node in range(N+2, 2*N+2):
            answer += (dists[node]-dists[node-1])*(weight_sum_2+1)
            weight_sum_2 -= sum(items[node])
            if not weight_sum_2:
                break
        answer += dists[node]-dists[N+1]
    print(answer)

main()
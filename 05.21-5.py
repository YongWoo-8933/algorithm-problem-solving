"""
백준 1806 부분합

1. 크루스칼 알고리즘을 기반으로 함
2. 최소 스패닝 트리를 구할 때, 가중치가 가장 큰 '마지막 간선을 추가하지 않는다'면
   최소한의 비용으로 노드들을 두 집합으로 구분할 수 있게됨
3. 따라서 크루스칼 알고리즘을 통해 구한 유지비 합에서 마지막에 더했던 cost값을 뺀값을 출력

10 15
5 1 3 5 10 7 4 9 2 8

2
"""
N, S = map(int, input().split())
lst = [*map(int, input().split())]
sum_lst = []
start_idx = 0
min_length = float("inf")
for i in range(N):
    n = lst[i]
    for j in range(start_idx, len(sum_lst)):
        sum_lst[j] += n
        if sum_lst[j]>=S:
            min_length = min(min_length, i-j+1)
            start_idx = j+1
    sum_lst.append(n)
print(min_length if min_length!=float("inf") else 0)

        


    


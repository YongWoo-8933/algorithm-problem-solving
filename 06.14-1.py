"""
백준 28707 배열정렬

1. cost가 가장 적게되는 sorting조합을 찾아야 하는데,
   매커니즘이 다익스트라 알고리즘과 비슷하다는 것을 찾는게 관건
2. **다익스트라 알고리즘에서 각 node를 배열의 상태로 두는게 포인트**
3. 원래 다익스트라는 1 -> 2의 cost가 10 이런식이라면,
   여기서는 [1, 3, 2] -> [1, 2, 3]의 cost가 10 이런식인것
4. 따라서 각 node를 리스트의 tuple형태로 두고 다익스트라 알고리즘 진행
"""
from heapq import heappop, heappush

N = int(input())
lst = [0, *map(int, input().split())]
M = int(input())
costs = [[*map(int, input().split())] for _ in range(M)]

start_tuple = tuple(lst)
visited = {start_tuple: 0}
q = []
heappush(q, (0, start_tuple))
while q:
    total_cost, t = heappop(q)
    for li, ri, cost in costs:
        temp = list(t)
        temp[li], temp[ri] = temp[ri], temp[li]
        new_t = tuple(temp)
        if new_t in visited and total_cost+cost>=visited[new_t]:
            continue
        visited[new_t] = total_cost+cost
        heappush(q, (total_cost+cost, new_t))

sorted_tuple = tuple(sorted(lst))
print(visited[sorted_tuple] if sorted_tuple in visited else -1)













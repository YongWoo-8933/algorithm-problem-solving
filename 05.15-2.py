"""
백준 12851 숨바꼭질 2

1. BFS를 통한 완전탐색
2. 동생의 위치가 더 작거나 같으면 걸어가는 경우가 항상 가장 빠르므로 N-K
3. 동생의 위치가 더 클경우, 걷는 경우와 순간이동하는 경우를 queue에 추가
4. check 리스트로 각 node에서의 최소시간을 update해 queue에 중복 없게함
5. 최단시간이 나오면 그 후로는 종료
"""
from collections import deque
 
N, K = map(int, input().split())
if N>=K:
    print(N-K, 1)
else:
    q = deque([(0, N)])
    check = [10**6] * (K+2)
    check[N] = 0
    count = 0
    while q:
        total_sec, node = q.popleft()
        if node == K:
            count += 1
            continue
        total_sec += 1
        for next_node in [node+1, node-1, node*2]:
            if 0 <= next_node < K+2:
                if total_sec <= check[next_node]:
                    check[next_node] = total_sec
                    q.append((total_sec, next_node))
    print(check[K], count)



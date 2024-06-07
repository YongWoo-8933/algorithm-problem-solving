"""
백준 30805 사전 순 최대 공통 부분 수열

1. 먼저 각 수열의 원소를 모두 탐색하며 겹치는 값, 겹치는 위치(index)를 찾음
2. 겹치는 값에 -를 붙이고 tuple형태로 heappush함으로써 최대힙 형태로 저장
3. q에서 값을 하나씩 heappop해나가며 answer list에 추가함
4. 이때 마지막으로 나왔던 A, B원소 index를 기억하며 이 index이후의 값들만 answer에 추가
"""
from heapq import heappush, heappop

N = int(input())
A = [*map(int, input().split())]
M = int(input())
B = [*map(int, input().split())]

q = []
for ai in range(N):
    for bi in range(M):
        if A[ai]==B[bi]:
            heappush(q, (-A[ai], ai, bi))

answer = []
ap, bp = -1, -1

while q:
    v, ai, bi = heappop(q)
    if ai>ap and bi>bp:
        answer.append(-v)
        ap, bp = ai, bi

print(len(answer))
if len(answer):
    print(*answer)








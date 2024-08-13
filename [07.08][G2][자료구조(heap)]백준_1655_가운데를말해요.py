"""
백준 1655 가운데를 말해요 (골드2)

시도 1. 이분 탐색으로 정렬되는 위치에 수 삽입
    => 이분탐색 자체는 시간문제가 없음
    => insert() 하는 과정에서 O(n)의 시간복잡도로 결국 O(n^2)의 시간복잡도가 됨
    => 시간 초과

시도 2. heap 두개를 이용한 풀이
1. min - max heap을 한개씩 운용하는게 포인트
2. 중앙값을 기준으로 이보다 작은 절반은 max heap, 큰 절반은 min heap에 저장해나감
3. 만약 max heap과 min heap의 길이에 불균형이 생긴다면,
   다시 균형을 이룰때까지 많은쪽에서 적은쪽으로 heap pop을 해줌
"""
from sys import stdin
from heapq import heappop, heappush
from bisect import bisect_left

# 시도 1
N = int(stdin.readline())
q = []
cnt = 0
for i in stdin:
    x = int(i)
    q.insert(bisect_left(q, x), x)
    cnt += 1
    if cnt%2:
        print(q[cnt//2])
    else:
        print(q[cnt//2-1])

# 시도 2
N = int(stdin.readline())
first_num = int(stdin.readline())
print(first_num)

min_hq, max_hq = [], [-first_num]
cnt = 1
for i in stdin:
    x = int(i)
    cnt += 1
    if x<=-max_hq[0]:
        heappush(max_hq, -x)
    else:
        heappush(min_hq, x)
    
    center_cnt = cnt//2+1 if cnt%2 else cnt//2

    while len(max_hq)<center_cnt:
        heappush(max_hq, -heappop(min_hq))
    while len(max_hq)>center_cnt:
        heappush(min_hq, -heappop(max_hq))

    print(-max_hq[0])



"""
백준 1202 보석 도둑

1. 가지고 있는 가방을 용량 오름차순으로 정렬
2. 주어진 보석을 무게 내림차순으로 정렬
3. temp list 생성 -> temp는 현재 가방의 용량보다 작거나 같은 무게의 보석을 넣어두는 용도
3. 가방 용량순으로 for문 진행, 각 iter에서 while문을 실행해 가장 가벼운 보석을 pop하고,
   pop한 보석의 무게가 가방의 용량보다 작거나 같다면 temp에 해당 보석의 value를 heappush
4. 가방용량보다 작은 무게의 보석이 없다면, while문 종료
5. temp에 보석이 있다면, heappop으로 가장 비싼 보석을 꺼내 답에 합산함
"""
from sys import stdin
from heapq import heappop, heappush

N, K = map(int, stdin.readline().split())
gems = [[*map(int, stdin.readline().split())] for _ in range(N)]
bags = [int(i) for i in stdin]
gems.sort(reverse=True)
bags.sort()
answer = 0
temp = []
for bag in bags:
    while gems and gems[-1][0]<=bag:
        weight, value = gems.pop()
        heappush(temp, -value)
    if temp:
        answer += -heappop(temp)
print(answer)

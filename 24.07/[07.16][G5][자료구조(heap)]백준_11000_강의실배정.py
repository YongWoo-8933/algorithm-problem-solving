"""
백준 11000 강의실 배정 (골드5)

1. 강의를 시작시간 순으로 정렬
2. 힙을 만들고 강의의 종료시간을 집어넣음
3. 힙에서 가장 작은값(가장 빨리 끝나는 시간의 강의)이 강의 시작시간보다
   작거나 같다면 강의실에서 나가는 것으로 보고 heap에서 값을 pop
4. 힙에 저장된 강의의 수 = 강의실의 수이므로 매 순회마다 answer 갱신
"""
from heapq import heappop, heappush
from sys import stdin

N = int(stdin.readline())
lst = [[*map(int, i.split())] for i in stdin]
lst.sort()
answer = 0
hq = []
for s, e in lst:
    while hq and hq[0]<=s:
        heappop(hq)
    heappush(hq, e)
    answer = max(answer, len(hq))
print(answer)

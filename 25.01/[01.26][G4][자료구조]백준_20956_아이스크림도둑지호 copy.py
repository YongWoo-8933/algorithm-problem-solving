"""
백준 20956 아이스크림 도둑 지호 (골드4)

1. 아이스크림을 양에따라 sort 및 인덱싱
2. dq를 운영해 같은 양의 아이스크림 전부 dq에 넣기
3. 순서가 뒤바뀐지 여부에따라 dq의 앞에서 pop할지 뒤에서 pop할지 정해 출력
4. 먹은 아이스크림 양이 7의 배수면 순서를 뒤바꾼 여부 변경
"""

from sys import stdin
from collections import deque

def main():
    N, M = map(int, stdin.readline().split())
    icecream = [*map(int, stdin.readline().split())]
    for i in range(N):
        icecream[i] = (icecream[i], i+1)
    icecream.sort()
    dq = deque()
    is_reversed = False
    for _ in range(M):
        if not dq:
            value, idx = icecream.pop()
            dq.appendleft((value, idx))
            while icecream and icecream[-1][0]==value:
                dq.appendleft(icecream.pop())
        if is_reversed:
            value, idx = dq.pop()
        else:
            value, idx = dq.popleft()
        print(idx)
        if value%7==0:
            is_reversed = not is_reversed

main()
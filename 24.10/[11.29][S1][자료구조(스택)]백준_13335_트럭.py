"""
백준 13335 트럭 (실버1)

1. deque을 만들어 다리로 생각하고, 매 단위시간마다 일어나는 일을 구현
"""
from collections import deque

def main():
    _, w, L = map(int, input().split())
    lst = [*map(int, input().split())][::-1]
    bridge = deque([0]*w)
    cur_weight = 0
    answer = 0
    while lst or cur_weight:
        answer += 1
        cur_weight -= bridge.popleft()
        if not lst:
            continue
        if cur_weight+lst[-1]<=L:
            cur_weight += lst[-1]
            bridge.append(lst.pop())
        else:
            bridge.append(0)
    print(answer)

main()
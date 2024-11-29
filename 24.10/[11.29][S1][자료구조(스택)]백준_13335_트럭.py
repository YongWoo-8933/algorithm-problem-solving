"""
백준 2665 미로만들기 (골드4)

1. heapq로 색을 바꾼 수가 적은 경우부터 BFS로 돌려 오른쪽 아래에 도달하면 종료
"""
from collections import deque

def main():
    n, w, L = map(int, input().split())
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
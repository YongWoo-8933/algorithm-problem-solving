"""
백준 25596 마트료시카 박스 II (골드4)

1. 문제 이해하는게 가장 중요함
2. q를 사용해 모든 박스를 순회하며 체크해나가면 됨
"""
from sys import stdin
from collections import deque

def main():
    N, M, K = map(int, stdin.readline().split())
    boxes = [deque()]
    for i in stdin:
        tmp = deque([*map(int, i.split())])
        tmp.popleft()
        boxes.append(tmp)
    for idx in range(1, N+1):
        while len(boxes[idx])>M:
            if K==0:
                print(0)
                exit()
            K -= 1
            new_box = deque()
            for _ in range(M):
                new_box.append(boxes[idx].pop())
            boxes[idx].appendleft(len(boxes))
            boxes.append(new_box)
    print(1)
    print(len(boxes)-(N+1))
    for l in boxes[1:]:
        l.appendleft(len(l))
        print(*l)

main()
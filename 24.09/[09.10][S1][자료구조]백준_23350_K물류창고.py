"""
백준 23350 K물류창고 (실버1)

1. 컨베이어 벨트를 deque으로 구현하고
2. 현재 적재함을 stack으로 구현해
3. 조건에 맞게 조건문 분기 > 무게를 더해나감
"""
from sys import stdin
from collections import deque

def main():
    _, M = map(int, stdin.readline().split())
    q = deque()
    containers = [0]*(M+1)
    for i in stdin:
        priority, weight = map(int, i.split())
        containers[priority] += 1
        q.append([priority, weight])
    cur_priority = M
    answer = 0
    stack = []
    while q:
        priority, weight = q.popleft()
        if cur_priority==priority:
        # 적재 가능
            temp = []
            while stack and stack[-1]<weight:
                temp.append(stack.pop())
            stack.append(weight)
            answer += 2*sum(temp)+weight
            temp.sort()
            while temp:
                stack.append(temp.pop())
            containers[priority] -= 1
            if containers[priority]==0:
                cur_priority -= 1
                stack = []
        else:
        # 컨테이너 처음으로 보내기
            q.append([priority, weight])
            answer += weight
    print(answer)
        
main()
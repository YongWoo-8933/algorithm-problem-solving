"""
백준 20055 컨베이어 벨트 위의 로봇 (골드 5)

1. deque의 rotate함수를 이용해 컨베이어 벨트의 회전을 구현
2. 각 단계 조건에 맞게 수행 후 결과 반환
"""
from sys import stdin
from collections import deque

def main():
    N, K = map(int, stdin.readline().split())
    conveyor_belt = deque([[int(i), False] for i in stdin.readline().split()])
    cnt = 0
    iteration = 0
    while cnt<K:
        # 컨베이어 회전 + 출구쪽 로봇 내보내기
        conveyor_belt.rotate(1)
        conveyor_belt[N-1][1] = False
        # 로봇 이동
        if conveyor_belt[N-2][1] and conveyor_belt[N-1][0]>=1:
            conveyor_belt[N-2][1] = False
            conveyor_belt[N-1][0] -= 1
            if conveyor_belt[N-1][0]==0:
                cnt += 1
        for i in range(N-3, -1, -1):
            if conveyor_belt[i][1] and conveyor_belt[i+1][0]>=1 and not conveyor_belt[i+1][1]:
                conveyor_belt[i][1] = False
                conveyor_belt[i+1][0] -= 1
                conveyor_belt[i+1][1] = True
                if conveyor_belt[i+1][0]==0:
                    cnt += 1
        # 새 로봇 넣기
        if conveyor_belt[0][0]>=1 and not conveyor_belt[0][1]:
            conveyor_belt[0][0] -= 1
            conveyor_belt[0][1] = True
            if conveyor_belt[0][0]==0:
                cnt += 1
        # cycle 추가
        iteration += 1
    print(iteration)

main()
"""
백준 5175 문제없는 문제 (골드 5)

1. 비트마스킹을 사용해 어떤 알고리즘이 모였는지 확인
2. 각 문제가 뽑히냐 vs 뽑히지 않냐의 두 경우이므로 총 2^N가지 경우가 나옴
3. N <= 20이므로 경우의 수는 최대 2^20 = 1,048,576 => 브루트포스 가능
4. queue 또는 재귀로 모든 경우 체크
"""
from sys import stdin
from collections import deque

def main():
    for tc in range(1, int(stdin.readline())+1):
        M, N = map(int, stdin.readline().split())
        lst = []
        for _ in range(N):
            bit = 0
            for num in map(int, stdin.readline().split()):
                bit = bit | (1<<(num-1))
            lst.append(bit)
        all_collected_bit = 2**M-1
        q = deque([(0, 0, "")])
        answer_cnt, answer_lst = N, []
        while q:
            idx, collected_bit, problems = q.popleft()
            len_problems = len(problems)
            # 모든 알고리즘 다 모았는지 확인
            if collected_bit==all_collected_bit:
                if len_problems==answer_cnt:
                    answer_lst.append(problems)
                elif len_problems<answer_cnt:
                    answer_cnt = len_problems
                    answer_lst = [problems]
                continue
            # 마지막 idx면 패스
            if idx==N:
                continue
            # 이번 문제 미포함
            q.append((idx+1, collected_bit, problems))
            # 이번 문제 포함
            new_bit = collected_bit | lst[idx]
            new_problems = problems+chr((ord("A")+idx))
            q.append((idx+1, new_bit, new_problems))
        
        answer_lst.sort()
        pb = " ".join(answer_lst[0])
        print(f"Data Set {tc}: {pb}")
        print("")

main()
"""
백준 5179 우승자는 누구? (실버 2)

** 1. 틀린 문제를 총점에 추가할 때 맞힌 이후 틀린문제는 무시해야 함
2. 1번을 잘 고려해 적당히 list와 dict를 활용하면 됨.
"""
from sys import stdin

for k in range(int(stdin.readline())):
    M, N, P = map(int, stdin.readline().split())
    solved_problems = [set() for _ in range(P+1)]
    wrong_problems = [{} for _ in range(P+1)]
    total_scores = [0 for _ in range(P+1)]
    print(f"Data Set {k+1}:")
    for _ in range(N):
        p, m, t, j = stdin.readline().strip().split()
        p, t, j = map(int, (p, t, j))
        # 맞춘 이후는 생각하지 않음
        if m not in solved_problems[p]:
            # 틀렸던 문제에 없으면 초기화
            if m not in wrong_problems[p]:
                wrong_problems[p][m] = 0
            # 맞춤
            if j:
                solved_problems[p].add(m)
                total_scores[p] += t+wrong_problems[p][m]
            # 틀림
            else:
                wrong_problems[p][m] += 20
    answer = []
    for p in range(1, P+1):
        answer.append((p, len(solved_problems[p]), total_scores[p]))
    answer.sort(key=lambda x: (-x[1], x[2]))
    for i in answer:
        print(*i)
    print("")





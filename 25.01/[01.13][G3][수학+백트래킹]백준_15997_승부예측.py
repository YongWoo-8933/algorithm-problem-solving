"""
백준 15997 승부예측 (골드3)

1. 백트래킹을 통해 나올 수 있는 모든 경우의 수에서의 승점 분포를 정렬
2. 승점 분포가 정해졌을때, 각 국가별 진출 확률 계산 후 answer에 합산
"""

from sys import stdin
from itertools import combinations

def main():
    nations = [*stdin.readline().strip().split()]
    probabilities = [[[[0.0]*3] for __ in range(4)] for _ in range(4)]
    for i in stdin:
        nation1, nation2 = i.split()[:2]
        nation1_idx, nation2_idx = nations.index(nation1), nations.index(nation2)
        win, draw, lose = map(float, i.split()[2:])
        probabilities[nation1_idx][nation2_idx] = [win, draw, lose]
        probabilities[nation2_idx][nation1_idx] = [lose, draw, win]
    answer = [0.0]*4
    matchs = [*combinations([0, 1, 2, 3], 2)]
    scores = [0, 0, 0, 0]

    def back_tracking(match_idx: int, prob: float):
        if match_idx==6:
            copied = [(scores[i], i) for i in range(4)]
            copied.sort(reverse=True)
            if copied[0][0]>copied[1][0]==copied[2][0]>copied[3][0]:
                answer[copied[0][1]] += prob
                answer[copied[1][1]] += prob/2
                answer[copied[2][1]] += prob/2
            elif copied[0][0]==copied[1][0]==copied[2][0]>copied[3][0]:
                answer[copied[0][1]] += prob*2/3
                answer[copied[1][1]] += prob*2/3
                answer[copied[2][1]] += prob*2/3
            elif copied[0][0]>copied[1][0]==copied[2][0]==copied[3][0]:
                answer[copied[0][1]] += prob
                answer[copied[1][1]] += prob/3
                answer[copied[2][1]] += prob/3
                answer[copied[3][1]] += prob/3
            elif copied[0][0]==copied[1][0]==copied[2][0]==copied[3][0]:
                answer[copied[0][1]] += prob/2
                answer[copied[1][1]] += prob/2
                answer[copied[2][1]] += prob/2
                answer[copied[3][1]] += prob/2
            else:
                answer[copied[0][1]] += prob
                answer[copied[1][1]] += prob
            return
        nation1_idx, nation2_idx = matchs[match_idx]
        # 국가1 승
        scores[nation1_idx] += 3
        back_tracking(match_idx+1, prob*probabilities[nation1_idx][nation2_idx][0])
        scores[nation1_idx] -= 3
        # 무
        scores[nation1_idx] += 1
        scores[nation2_idx] += 1
        back_tracking(match_idx+1, prob*probabilities[nation1_idx][nation2_idx][1])
        scores[nation1_idx] -= 1
        scores[nation2_idx] -= 1
        # 국가1 패
        scores[nation2_idx] += 3
        back_tracking(match_idx+1, prob*probabilities[nation1_idx][nation2_idx][2])
        scores[nation2_idx] -= 3
    
    back_tracking(0, 1.0)
    print(*answer)

main()
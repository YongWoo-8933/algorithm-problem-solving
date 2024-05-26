"""
백준 2342 Dance Dance Revolution

1. 평범한 greedy 알고리즘으로 가기에는 경우가 좀 더 많음
   (당장은 왼쪽발로 가는게 더 낫더라도, 전체적으로는 비용이 많은 경우도 있음)
2. 우선 방향 i > j로 가는 모든 경우에 대한 cost를 2차원 배열로 정리
   (costs[i][j] 형식)
3. 발의 방향이 상관없으므로, 발의 위치는 맨처음 (0, 0)을 제외하면 항상 아래 조합중 하나임
   (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)
4. 따라서 눌러야할 각 방향표 버튼에 대해 모든 케이스의 누적 cost를 쌓아가는 방식으로 진행
   ex) (0, 1) -> (0, 2) 인경우 / (0, 1) -> (2, 1) 인경우 등을 각각 쌓음
   10가지 모든경우에 대해 나올수 있는 경우는 많아봐야 10가지, 중복되는 경우 cost가 낮은쪽 선택
"""
def case_index(a: int, b: int) -> int:
    for i in range(10):
        comb = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)][i]
        if a in comb and b in comb:
            return i

def case_comb(idx: int) -> tuple:
    return [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)][idx]

directions = [*map(int, input().split())]
directions.pop()
costs = [[2]*5 for _ in range(5)]
for i in range(1, 5):
    for j in range(1, 5):
        if i==j:
            costs[i][j] = 1
        elif abs(i-j)==2:
            costs[i][j] = 4
        else:
            costs[i][j] = 3
feet_case_dict = {case_index(0, directions[0]): 2}
for direction in directions[1:]:
    new_dict = {}
    for case_idx, total_cost in feet_case_dict.items():
        lfoot, rfoot = case_comb(case_idx)
        for new_idx, new_cost in zip([case_index(direction, rfoot), case_index(lfoot, direction)], [costs[lfoot][direction], costs[rfoot][direction]]):
            if new_idx in new_dict:
                new_dict[new_idx] = min(new_dict[new_idx], total_cost+new_cost)
            else:
                new_dict[new_idx] = total_cost+new_cost
    feet_case_dict = new_dict
print(min(feet_case_dict.values()))


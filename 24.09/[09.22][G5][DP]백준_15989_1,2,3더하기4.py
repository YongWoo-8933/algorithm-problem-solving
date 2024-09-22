"""
백준 15989 1, 2, 3 더하기 4 (골드 5)

1. dp로 가되 각 iter에서 1이 포함된 덧셈, 2/3만 포함된 덧셈, 3만 있는 덧셈으로 나누어 저장
"""
from sys import stdin

def main():
    dp_table = [0, 1, 2, 3]
    dp1_three = 0
    dp2_two, dp2_three = 1, 0
    dp3_one, dp3_two, dp3_three = 2, 0, 1
    for _ in range(4, 10001):
        new_dp3_one = dp3_one+dp3_two+dp3_three
        new_dp3_two = dp2_two+dp2_three
        new_dp3_three = dp1_three
        dp1_three = dp2_three
        dp2_two, dp2_three = dp3_two, dp3_three
        dp3_one, dp3_two, dp3_three = new_dp3_one, new_dp3_two, new_dp3_three
        dp_table.append(dp3_one+dp3_two+dp3_three)

    for _ in range(int(stdin.readline())):
        print(dp_table[int(stdin.readline())])

main()
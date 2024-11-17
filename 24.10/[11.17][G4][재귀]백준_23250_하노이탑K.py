"""
백준 9753 짝 곱 (실버2)

1. 주어진 K값에서 1씩 더해가며 소인수가 4개인 수를 찾으면 됨
"""

def main():
    N, K = map(int, input().split())
    move_nums = [0]
    for _ in range(N):
        move_nums.append(move_nums[-1]*2+1)

    def recur(num: int, fr: int, to: int, k: int):
        if k<=move_nums[num-1]:
            recur(num-1, fr, 6-fr-to, k)
        elif k==move_nums[num-1]+1:
            print(f"{fr} {to}")
        else:
            recur(num-1, 6-fr-to, to, k-move_nums[num-1]-1)

    recur(N, 1, 3, K)

main()
"""
백준 23250 하노이 탑 K (골드4)

1. 하노이탑 기본 로직에서 개수에 유의해 재귀를 진행하면 됨
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
"""
백준 30459 현수막 걸기 (골드5)

1. 나올 수 있는 밑변 값을 중복없이 모두 구함
2. 각 밑변 값에대해, 이분탐색으로 구한 높이를 곱해 넓이를 구함
"""

def main():
    N, M, R = map(int, input().split())
    pos = sorted(map(int, input().split()))
    heights = sorted(map(int, input().split()))
    bottom_lens = set()
    for i in range(N):
        for j in range(i+1, N):
            bottom_lens.add(pos[j]-pos[i])
    answer = 0
    for bottom_len in bottom_lens:
        lp, rp = 0, M-1
        while lp<=rp:
            cp = (lp+rp)//2
            height = heights[cp]
            area = bottom_len*height/2
            if area==R:
                print(f"{R:.1f}")
                exit()
            elif area<R:
                lp = cp+1
            else:
                rp = cp-1
        area = bottom_len*heights[rp]/2
        if area==R:
            print(f"{R:.1f}")
            exit()
        elif area<R:
            answer = max(answer, area)
    print(f"{answer:.1f}" if answer>0 else -1)

main()
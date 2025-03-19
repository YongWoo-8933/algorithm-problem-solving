"""
백준 30645 인형 전시 (실버2)

1. 높이가 같은 인형은 최대 한 행만큼만 보일 수 있음을 유의해서 카운트하면 됨
"""

def main():
    H, W = map(int, input().split())
    N = int(input())
    heights = [0]*1000001
    for height in map(int, input().split()):
        if heights[height]==W:
            N -= 1
        else:
            heights[height] += 1
    print(min(N, H*W))

main()
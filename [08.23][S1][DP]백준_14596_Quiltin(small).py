"""
백준 14596 Quilting (Small) (실버 1)

예제 입력 1 
4 3
0 79 240
10 110 230
9 130 213
30 70 235
50 62 237
16 58 99
25 120 170
90 120 240
예제 출력 1 
450
"""
from sys import stdin

def main():
    H, W = map(int, stdin.readline().split())
    # B1 = [[*map(int, stdin.readline().split())] for _ in range(H)]
    # B2 = [[*map(int, i.split())] for i in stdin]
    B1 = [
        [0 ,79, 240],
        [10, 110, 23   ],
        [9 ,130 ,213   ],
        [30, 70 ,235   ],
    ]
    B2 = [
        [50, 62 ,237],
        [16, 58 ,99],
        [25, 120, 170],
        [90, 120, 240],
    ]
    dp = [0]*W
    INF = (255**2)*10
    for row in range(H):
        new_dp = [0]*W
        for col in range(W):
            min_value = INF
            for c in [col-1, col, col+1]:
                if 0<=c<W:
                    min_value = min(min_value, dp[c])
            new_dp[col] = min_value+(B1[row][col]-B2[row][col])**2
        dp = new_dp
    print(min(dp))

main()
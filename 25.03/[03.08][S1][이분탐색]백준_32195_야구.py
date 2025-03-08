"""
백준 32195 야구 (실버1)

1. 파울볼부터 카운트
2. 나머지 내야 or 홈런볼들은 각각 몇미터 갔는지 따로 저장
3. 저장된 리스트 정렬
4. r이 주어졌을때, 정렬된 리스트에서 몇번째에 위치해있는지 이분탐색으로 찾기
5. 몇번째 위치해있는지 알면 내야와 홈런볼 갯수를 알 수 있음
"""
from sys import stdin
from bisect import bisect_left

def main():
    N = int(stdin.readline())
    no_foul_coords = []
    foul_cnt = 0
    for i in range(N):
        x, y = map(int, stdin.readline().split())
        if y<abs(x):
            foul_cnt += 1
        else:
            no_foul_coords.append((x, y))
    no_foul_cnt = len(no_foul_coords)
    radius_squares = [x**2+y**2 for x, y in no_foul_coords]
    radius_squares.sort()
    stdin.readline()
    for i in stdin:
        r_quare = int(i)**2
        n = bisect_left(radius_squares, r_quare+1)
        print(foul_cnt, n, no_foul_cnt-n)

main()
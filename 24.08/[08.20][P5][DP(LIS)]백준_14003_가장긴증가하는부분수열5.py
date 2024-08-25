"""
백준 14003 가장 긴 증가하는 부분 수열 5 (플래티넘5)

1. LIS 알고리즘으로, 풀이가 어려워서 해답 참고
(https://velog.io/@veonico/%EB%B0%B1%EC%A4%80-14003.-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4-5-python%ED%8C%8C%EC%9D%B4%EC%8D%AC)
"""
from bisect import bisect_left

def main():
    input()
    INF = 1000000001
    lst = [*map(int, input().split())]
    num = [-INF]
    num_index = [(-INF, 0)]
    largest_num_idx = 0
    for n in lst:
        if n>num[-1]:
            largest_num_idx = len(num_index)
            num_index.append((n, len(num)))
            num.append(n)
        else:
            idx = bisect_left(num, n)
            num[idx] = n
            num_index.append((n, idx))
    last_n, last_idx = num_index[largest_num_idx]
    answer = [last_n]
    for n, idx in num_index[largest_num_idx-1:0:-1]:
        if idx==last_idx-1:
            answer.append(n)
            last_idx = idx
    print(len(answer))
    answer.sort()
    print(*answer)

main()
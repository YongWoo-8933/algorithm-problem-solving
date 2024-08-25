"""
프로그래머스 풍선 터뜨리기

1. 풍선값중 최소값의 인덱스를 찾음
2. 해당 인덱스를 기준으로 풍선 그룹을 좌우로 분리
3. 분리된 각 그룹에서 최소값을 갱신하며 갱신될때마다 answer에 카운트
"""

def solution(a):
    min_index = a.index(min(a))
    left, right = [], []
    for i in range(min_index):
        left.append(a[i])
    for i in range(min_index+1, len(a)):
        right.append(a[i])
    answer = 1
    for lst in [left, right[::-1]]:
        min_value = 1000000000
        for x in lst:
            if x<min_value:
                min_value=x
                answer += 1
    return answer

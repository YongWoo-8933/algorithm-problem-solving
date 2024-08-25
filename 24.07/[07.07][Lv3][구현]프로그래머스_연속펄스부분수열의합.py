"""
프로그래머스 - 연속 펄스 부분 수열의 합
https://school.programmers.co.kr/learn/courses/30/lessons/161988
"""
def solution(sequence):
    N = len(sequence)
    lst1 = [(-1)**i*sequence[i] for i in range(N)]
    lst2 = [(-1)**(i+1)*sequence[i] for i in range(N)]
    answer = -100000
    for lst in (lst1, lst2):
        cur_max = -100000
        for num in lst:
            cur_max = num+max(cur_max, 0)
            answer = max(answer, cur_max)
    return answer
"""
프로그래머스 억억단을 외우자(level 3)
https://school.programmers.co.kr/learn/courses/30/lessons/138475

1. 결국 억억단에 등장하는 횟수 = 해당 수의 약수의 갯수
2. 따라서 에라토스테네스의 체를 쓸데와 유사하게 약수의 갯수 리스트를 만듦
3. 이후 각 범위에 따라 가장 약수의 갯수가 많은 수를 선정
"""
def solution(e, starts):
    lst = [0]*(e+1)
    for n in range(1, e+1):
        lst[n] += 1
        for m in range(n+1, e//n+1):
            lst[n*m] += 1
    max_value, max_cnt = e, lst[e]
    for v in range(e, 0, -1):
        if lst[v]>=max_cnt:
            max_cnt = lst[v]
            max_value = v
        lst[v] = max_value
    answer = [lst[i] for i in starts]
    return answer



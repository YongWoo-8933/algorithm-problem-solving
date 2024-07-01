"""
프로그래머스 <문자열 압축>
https://school.programmers.co.kr/learn/courses/30/lessons/60057

1. 모든 경우의 수를 탐색하면 됨
2. 문자열 길이의 절반까지만 체크하면 됨(길이가 10이면 5까지만 이런식)
"""
def solution(s):
    n = len(s)
    answer = n
    for i in range(1, n//2+1):
        ps = s[:i]
        pcnt = 1
        p = i
        temp = ""
        while p<n:
            if p+i<n:
                x = s[p:p+i]
            else:
                x = s[p:]
            if ps==x:
                pcnt += 1
            else:
                if pcnt==1:
                    temp += ps
                else:
                    temp += str(pcnt)+ps
                    pcnt = 1
                ps = x
            p += i
        if pcnt==1:
            temp += ps
        else:
            temp += str(pcnt)+ps
        answer = min(answer, len(temp))
                
    return answer
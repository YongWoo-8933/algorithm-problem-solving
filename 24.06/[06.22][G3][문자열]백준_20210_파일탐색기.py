"""
백준 20210 파일 탐색기 (골드3)

1. functools의 cmp_to_key 함수를 통해 두 객체의 대소비교를 customizing하는게 관건
2. customizing한 대소비교 함수를 sort() 메소드의 key값에 넣어주면 됨

https://www.acmicpc.net/source/53568956 풀이가 기가막히고 코가막힘
"""
from sys import stdin
from functools import cmp_to_key

def str_2_list(x: str) -> list:
    result = [x[0]]
    for i in range(1, len(x)):
        s = x[i]
        p_s = result[-1]
        if (s.isdigit() and p_s[-1].isdigit()) or (not s.isdigit() and not p_s[-1].isdigit()):
            result[-1] = p_s+s
        else:
            result.append(s)
    return result

def compare(a: str, b: str) -> int:
    if a.isdigit() and b.isdigit():
        # 숫자 vs 숫자
        if int(a)==int(b):
            if len(a)<len(b):
                return -1
            elif len(a)>len(b):
                return 1
            else:
                return 0
        elif int(a)<int(b):
            return -1
        else:
            return 1
    elif a.isdigit() and not b.isdigit():
        # 숫자 vs 문자
        return -1
    elif not a.isdigit() and b.isdigit():
        # 문자 vs 숫자
        return 1
    else:
        # 문자 vs 문자
        p = 0
        while p<len(a) and p<len(b):
            s_a, s_b = a[p], b[p]
            if s_a.upper()<s_b.upper():
                return -1
            elif s_a.upper()>s_b.upper():
                return 1
            elif s_a.isupper() and s_b.islower():
                return -1
            elif s_a.islower() and s_b.isupper():
                return 1
            else:
                p += 1
        if p==len(a) and p<len(b):
            return -1
        elif p<len(a) and p==len(b):
            return 1
        else:
            return 0

def mycmp(a: str, b: str) -> int:
    a_lst, b_lst = str_2_list(a), str_2_list(b)
    p = 0
    while p<len(a_lst) and p<len(b_lst):
        v = compare(a_lst[p], b_lst[p])
        if v==0:
            p+=1
        else:
            return v
    if p==len(a_lst) and p<len(b_lst):
        return -1
    elif p<len(a_lst) and p==len(b_lst):
        return 1
    else:
        return 0

N = int(stdin.readline())
lst = [i.strip() for i in stdin]
lst.sort(key=cmp_to_key(mycmp))
print(*lst)


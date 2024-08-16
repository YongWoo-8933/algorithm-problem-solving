"""
백준 6581 HTML (골드5)

1. 하드코딩 구현
2. 80자 넘는지 확인할 때 띄어쓰기까지 고려하는것 주의
"""
from sys import stdin

lst = []
for i in stdin:
    for j in i.strip().split():
        lst.append(j)
answer = ""
hr = "-"*80
for s in lst:
    if s[0]=="<":
        if s[1]=="b":
            print(answer)
            answer = ""
        elif s[1]=="h":
            if answer:
                print(answer)
            answer = ""
            print(hr)
    else:
        if len(answer)+len(s)+1>80:
            print(answer)
            answer = s
        else:
            if answer:
                answer += " "
            answer += s
if answer:
    print(answer)
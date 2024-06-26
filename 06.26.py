"""
백준 14725 개미굴 (골드3)

1. 각 개미의 경로를 list 형태로 저장
2. 사전순으로 정렬
3. 각 개미의 경로를 순회하기 시작
4. p_lst는 이전 개미의 순회 경로로 설정. 처음에는 빈 리스트
5. 이번 개미의 순회 경로를 저장할 n_p_lst 생성
6. p_lst를 순회하며 현재 개미의 경로중 이전 개미의 경로와 겹치는 부분을 패스
7. 겹치지 않는 나머지 부분을 층에 맞게 "--"를 붙여 출력
8. p_lst를 n_p_lst로 갱신하며 다음 개미의 경로로 이동
"""
from sys import stdin        

N = int(stdin.readline())
lst = []
for _ in range(N):
    lst.append([*stdin.readline().strip().split()][1:])
lst.sort()

p_lst = []
for cur in lst:
    p = 0
    n_p_lst = []
    while p<len(p_lst) and p<len(cur) and p_lst[p]==cur[p]:
        n_p_lst.append(cur[p])
        p += 1
    while p<len(cur):
        print("--"*p + cur[p])
        n_p_lst.append(cur[p])
        p += 1
    p_lst = n_p_lst

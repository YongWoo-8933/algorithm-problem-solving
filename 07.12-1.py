"""
백준 1339 단어 수학 (골드4)

** 많은 시행착오를 겪음..
** 기본적으로 가장 높은 자리에 위치한 문자가 높은 숫자가 매칭되어야함
** 여기서 중요한건 같은 자리수에 위치한 문자사이 서열을 어떻게 정하는가 하는것
** 결론적으로 이후 등장할 문자까지 모두 고려한 카운트가 진행되어야함

1. dict를 하나 만드는데, {"A": 10, "B": 20} 이런식으로 문자와 점수를 매칭
2. 점수는 10^(자리수-1)만큼 부여
   ex) ABCE + BAE 라면 A는 총 10^(4-1) + 10^(2-1) = 1010점을 가지게 됨
3. 이 점수는 해당 문자열이 숫자로 치환되었을때 등장하는 빈도수와 같음
   ex) 위 예에서 A=9로 둔다면 9가 1010번 등장하므로 9090만큼의 값을 가짐
4. dict 설정이 끝나면 점수가 높은순으로 나열하고
5. 점수 높은 순으로 숫자를 매칭해 합산 후 출력
"""
from sys import stdin

N = int(stdin.readline())
lst = [i.strip() for i in stdin]
a_dict = {}
for s in lst:
    for digit in range(len(s), 0, -1):
        x = s[len(s)-digit]
        if x in a_dict:
            a_dict[x] += 10**(digit-1)
        else:
            a_dict[x] = 10**(digit-1)

num = 9
answer = 0
temp = sorted(a_dict.items(), key=lambda x: -x[1])
for s, cnt in temp:
    answer += num*cnt
    num -= 1
print(answer)
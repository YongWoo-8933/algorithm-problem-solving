"""
백준 14718 용감한 용사 진수 (골드 4)

N명의 적 병사가 있다. 적의 각 병사는 힘, 민첩, 지능의 3가지 능력치를 가진다. 
용감한 용사 진수도 힘, 민첩, 지능의 3가지 능력치를 가진다.

적의 각 병사에 대해,

적 병사가 가진 힘보다 진수의 힘이 크거나 같고,
적 병사가 가진 민첩보다 진수의 민첩이 크거나 같고,
적 병사가 가진 지능보다 진수의 지능이 크거나 같으면,
진수는 그 적 병사를 이길 수 있다.

용감한 용사 진수에게 스탯 포인트를 주면 똑똑한 진수는 
자기가 최대한 많은 적을 이길 수 있도록 스탯 포인트를 스스로 분배한다.

N명의 병사들 스탯이 주어졌을 때, 진수가 적어도 K명의 병사를 이길 수 있게 하는 
최소의 스탯 포인트를 구하여라.

입력
첫 번째 줄에는 N명의 병사 수와 용감한 용사 진수가 이겨야 할 K명의 병사 수가 주어진다. (1 ≤ K ≤ N ≤ 100)

두 번째 줄부터 N+1 번째 줄까지 각 줄마다 병사들의 힘, 민첩, 지능을 세 개의 음이 아닌 정수로 주어진다. (0 ≤ 힘, 민첩, 지능 ≤ 1000000)

출력
용감한 용사 진수가 적어도 K명의 병사를 이길 수 있게 하는 최소의 스탯 포인트를 출력하여라.

예제 입력 1 
3 3
10 5 5
5 10 5
5 5 10
예제 출력 1 
30
예제 입력 2 
3 1
234 23 342
35 4634 34
46334 6 789
예제 출력 2 
599
예제 입력 3 
3 2
30 30 30
10 500 10
50 10 50
예제 출력 3 
130
"""
from sys import stdin

def main():
    N, K = map(int, stdin.readline().split())
    lst, str_lst, dex_lst = [], [], []
    for i in stdin:
        s, d, i = map(int, i.split())
        lst.append((s, d, i))
        str_lst.append(s)
        dex_lst.append(d)
    str_lst.sort()
    dex_lst.sort()
    answer = float("inf")
    for str_stat in str_lst:
        for dex_stat in dex_lst:
            cnt = 0
            for s, d, i in lst:
                if str_stat+dex_stat+i>=answer:
                    break
                if str_stat>=s and dex_stat>=d:
                    cnt += 1
                if cnt>=K:
                    answer = min(answer, str_stat+dex_stat+i)
                    break
    print(answer)

main()
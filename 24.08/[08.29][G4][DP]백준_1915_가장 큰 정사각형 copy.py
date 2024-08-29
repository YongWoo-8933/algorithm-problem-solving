"""
백준 29618 미술 시간 (골드 3)

N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 한다.

N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.

수의 위치가 다르면 값이 같아도 다른 수이다.

입력
첫째 줄에는 수의 개수 N(1 ≤ N ≤ 2,000), 두 번째 줄에는 i번째 수를 나타내는 Ai가 N개 주어진다. (|Ai| ≤ 1,000,000,000, Ai는 정수)

출력
좋은 수의 개수를 첫 번째 줄에 출력한다.

예제 입력 1 
10
1 2 3 4 5 6 7 8 9 10
예제 출력 1 
8
"""

def main():
    N = int(input())
    lst_dict = {}
    for n in map(int, input().split()):
        if n in lst_dict:
            lst_dict[n] += 1
        else:
            lst_dict[n] = 1
    answer = 0
    if 0 in lst_dict:
        zero_cnt = lst_dict[0]
        del lst_dict[0]
        for value in lst_dict.values():
            answer += value*zero_cnt*(value-1)
    keys = list(lst_dict.keys())
    good_numbers = set()
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            v1, v2 = keys[i], keys[j]
            x = v1+v2
            if x in lst_dict and x not in good_numbers:
                good_numbers.add(x)
                answer += lst_dict[v1]*lst_dict[v2]*lst_dict[x]
    print(answer)
main()

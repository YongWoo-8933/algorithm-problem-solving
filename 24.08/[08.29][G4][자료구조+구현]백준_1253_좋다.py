"""
백준 1253 좋다 (골드4)

1. 각 수가 몇개씩 있는지 dict에 정리
2-1. 0이 있다면, 0끼리 좋은수를 만들수 있는 경우 체크
2-2. 0이 있다면, 0+다른수로 좋은수를 만들수 있는 경우 체크
3. 서로 다른수 두개로 좋은수 만들수 있는 경우 체크
"""

def main():
    input()
    numbers_dict = {}
    for n in map(int, input().split()):
        if n in numbers_dict:
            numbers_dict[n] += 1
        else:
            numbers_dict[n] = 1
    answer = 0
    good_numbers = set()
    if 0 in numbers_dict:
        zero_cnt = numbers_dict[0]
        del numbers_dict[0]
        none_zero_keys = list(numbers_dict.keys())
        # 0끼리 좋은 수 만드는 경우
        if zero_cnt>2:
            good_numbers.add(0)
            answer += zero_cnt
        # 0 + 다른수로 좋은 수 만드는 경우
        for key, value in numbers_dict.items():
            if value>1:
                good_numbers.add(key)
                answer += value
        numbers_dict[0] = zero_cnt
    else:
        none_zero_keys = list(numbers_dict.keys())
    # 다른 수끼리 더해 좋은 수 만드는 경우
    len_keys = len(none_zero_keys)
    for i in range(len_keys):
        for j in range(i+1, len_keys):
            v1, v2 = none_zero_keys[i], none_zero_keys[j]
            x = v1+v2
            if x in numbers_dict and x not in good_numbers:
                good_numbers.add(x)
                answer += numbers_dict[x]
    print(answer)
main()

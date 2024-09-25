"""
백준 16206 롤케이크 (실버 1)

1. 10의 배수 길이인 롤케이크부터 자르는게 이득 (자르는 횟수 +1개의 케이크 획득)
2. 똑같이 10의 배수라면 작은 크기의 케이크부터 자르는게 이득 (남은 횟수가 없다면, 10을 자르는게 20을 자르는것보다 이득)
3. 따라서 10의 배수/그 외 케이크를 분류하고, 10의 배수 케이크는 정렬해 작은 케이크부터 잘라가면 됨
"""

def main():
    _, M = map(int, input().split())
    tens, not_tens = [], []
    for i in input().split():
        num = int(i)
        if num%10:
            not_tens.append(num)
        else:
            tens.append(num)
    tens.sort(reverse=True)
    answer = 0
    while M and tens:
        num = tens.pop()
        if num//10-1<=M:
            answer += num//10
            M -= num//10-1
        else:
            answer += M
            M = 0
    while M and not_tens:
        num = not_tens.pop()
        answer += min(num//10, M)
        M -= min(num//10, M)
    print(answer)
main()
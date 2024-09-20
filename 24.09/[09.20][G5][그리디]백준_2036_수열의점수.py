"""
백준 2036 수열의 점수 (골드 5)

1. 주어진 수가 음수일때, 0일때, 1일때, 1보다 큰 양수일때 4가지 경우로 나눠 생각하면 쉬움
2. 1보다 큰 양수는 큰 수끼리 곱하고
3. 1은 따로 1개씩 더하고
4. 0은 음수가 하나 남았을때 없애주는 용도로 사용,
5. 음수는 절대값이 큰 수 두개씩 곱해주면 됨.
"""
from sys import stdin

def main():
    stdin.readline()
    positives, zero_exist, negatives = [], False, []
    score = 0
    for i in stdin:
        x = int(i)
        if x>1:
            positives.append(x)
        elif x==1:
            score += 1
        elif x==0:
            zero_exist = True
        else:
            negatives.append(x)
    positives.sort()
    negatives.sort(reverse=True)
    while positives:
        a = positives.pop()
        if positives:
            score += a*positives.pop()
        else:
            score += a
    while negatives:
        a = negatives.pop()
        if negatives:
            score += a*negatives.pop()
        elif not zero_exist:
            score += a
    print(score)
main()
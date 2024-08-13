"""
백준 2143 두 배열의 합 (골드3)

1. 누적합 방법을 이용해 A의 모든 i~j번째 합을 구함 (O(n^2))
2. 수열 A에대한 누적합을 진행하면서, dict를 하나 만들어 각 합값이 몇개인지 기록
   ex) 1~4수열합이 6, 4~5수열합이 1, 7~8수열합이 6이었다면, dict = {6: 2, 1: 1}
3. 수열 B에대한 누적합을 진행하면서, "T-누적합"이 위에서 만든 dict의 key로 존재한다면, 그 value값만큼 count
"""
T = int(input())
len_A, A = int(input()), [*map(int, input().split())]
len_B, B = int(input()), [*map(int, input().split())]
sum_A, sum_A_dict = [], {}
for i in range(len_A):
    x = A[i]
    for j in range(len(sum_A)):
        sum_A[j] += x
        if sum_A[j] in sum_A_dict:
            sum_A_dict[sum_A[j]] += 1
        else:
            sum_A_dict[sum_A[j]] = 1
    sum_A.append(x)
    if x in sum_A_dict:
        sum_A_dict[x] += 1
    else:
        sum_A_dict[x] = 1

sum_B = []
answer = 0
for i in range(len_B):
    x = B[i]
    for j in range(len(sum_B)):
        sum_B[j] += x
        if T-sum_B[j] in sum_A_dict:
            answer += sum_A_dict[T-sum_B[j]]
    sum_B.append(x)
    if T-x in sum_A_dict:
        answer += sum_A_dict[T-x]

print(answer)
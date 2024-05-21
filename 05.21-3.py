"""
백준 9252 LCS 2

1. LCS알고리즘 구현
2. dp테이블을 만들고 각 구간별 LCS길이(int값) 갱신
3. 테이블을 모두 채우고 나면, 거꾸로 읽어가면서 LCS문자열 산출
"""
A, B = input(), input()
len_A, len_B = len(A), len(B)
dp = [[0]*(len_B+1) for _ in range(len_A+1)]
for i in range(len_A):
    for j in range(len_B):
        dp[i+1][j+1] = dp[i][j]+1 if A[i]==B[j] else max(dp[i][j+1], dp[i+1][j])
print(dp[len_A][len_B])
if dp[len_A][len_B]:
    row, col = len_A, len_B
    answer = ""
    while row>=0 and col>=0:
        x = dp[row][col]
        if x==0:
            break
        if dp[row-1][col]==x:
            row -= 1
        elif dp[row][col-1]==x:
            col -= 1
        else:
            answer += A[row-1]
            row -= 1
            col -= 1
    print(answer[::-1])

        


    


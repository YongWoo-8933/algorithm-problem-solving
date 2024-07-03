"""
백준 2493 탑 (골드5)
** 오큰수 문제와 매커니즘이 비슷함(stack 풀이)
https://www.acmicpc.net/problem/17298

1. 오큰수에서는 stack내부 값에 따라 해당 idx값이 결정됐다면, 
   이 문제에서는 해당 idx값에 따라 stack 내부 값이 결정됨
"""
N = int(input())
towers = [*map(int, input().split())]
answer = [0]*N
s = []
for i in range(N-1, -1, -1):
    height = towers[i]
    while s and s[-1][1]<height:
        idx, h = s.pop()
        answer[idx] = i+1
    s.append((i, height))
print(*answer)




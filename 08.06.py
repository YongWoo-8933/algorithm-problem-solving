"""
백준 2437 저울 (골드2)

1. 주어진 무게를 정렬
2. 순서대로 더했을 때 나올 수 있는 값을 생각해보면 됨
"""
N = int(input())
lst = [*map(int, input().split())]
lst.sort()
S = 0
for n in lst:
    if n<=S+1:
        S += n
    else:
        break
print(S+1)



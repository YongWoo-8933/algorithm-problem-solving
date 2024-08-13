"""
백준 2705 팰린드롬 파티션

1. 가운데 수를 1~n까지 두며 왼쪽/오른쪽에 각각 똑같은 재귀 팰린드롬이 와야함
2. 따라서 dp로 쌓아가며 합치면 됨
"""
l=[1,1]
for i in range(2,1001):
    l+=[sum(l[:i//2+1])]
for i in range(int(input())):
    print(l[int(input())])
"""
백준 17298 오큰수 (골드4)
(* stack쓸 생각을 못해 해설 봄, stack이 쓰이는 문제 모양을 외워놔야할듯)

1. 주어진 배열의 오른쪽 끝부터 시작
2. stack을 만들고, stack의 마지막 수가 해당 값보다 작은 경우 모두 pop
3. NGE 리스트를 갱신하고 stack에 해당 값 추가
"""
N = int(input())
lst = [*map(int, input().split())]
NGE = [-1]*N
s = []
for i in range(N-1, -1, -1):
    while s and s[-1]<=lst[i]:
        s.pop()
    if s:
        NGE[i] = s[-1]
    s.append(lst[i])
print(*NGE)



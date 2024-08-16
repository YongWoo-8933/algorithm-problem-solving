"""
백준 2473 세 용액 (골드3)
-> 백준 2467 용액 문제의 확장형

1. 두 포인터로 용액합을 갱신하는 방식을 똑같음
2. 여기서는 포인터가 세개가 필요하므로, left pointer를 1~N-2까지 돌리며
   나머지 두 포인터(center, right)에 대해 각각 알고리즘 수행
"""
N = int(input())
lst = sorted(map(int, input().split()))
answer_value, answer_set = 10**10, (0, 0, 0)
for left in range(N-2):
    center, right = left+1, N-1
    while center<right:
        x = lst[left]+lst[center]+lst[right]
        if abs(x)<answer_value:
            answer_value = abs(x)
            answer_set = (lst[left], lst[center], lst[right])
        if x==0:
            print(lst[left], lst[center], lst[right])
            exit()
        elif x<0:
            center+=1
        else:
            right-=1
print(*answer_set)
"""
백준 30644 띠 정렬하기 (골드4)

1. 각 수에 index 저장해놓고 정렬
2. 순서대로 index 확인하며 바로 옆칸이 아니면 자르는 횟수 추가
"""
N = int(input())
lst = [*map(int, input().split())]
lst = [(lst[i], i) for i in range(N)]
lst.sort()
answer = 0
idx = lst[0][1]
for _, new_idx in lst:
    if abs(new_idx-idx)>1:
        answer += 1
    idx = new_idx
print(answer)
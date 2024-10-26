"""
백준 1914 하노이 탑 (골드5)

1. 점화식을 찾아 이동횟수 산출
2. 재귀를통해 이동경로 프린트 
"""

def recur(n: int, block_fr: int, block_to: int):
    global cnt, answer
    if n==1:
        print(f"{block_fr} {block_to}")
        return
    else:
        recur(n-1, block_fr, 6-block_fr-block_to)    
        print(f"{block_fr} {block_to}")
        recur(n-1, 6-block_fr-block_to, block_to)

N = int(input())
cnt = 0
for i in range(1, N+1):
    cnt = cnt*2+1
print(cnt)
if N<=20:
    recur(N, 1, 3)
"""
백준 2263 트리의 순회

1. post order list의 마지막 값이 항상 root인 점을 이용
2. in order list에서 root가 몇번째 인덱스에 있는지 확인
3. 2번을 수행하면, post order list와 in order list의 
   root/왼쪽서브트리/오른쪽서브트리를 구할 수 있음
4. 각 부분에 대해 재귀적으로 함수 실행
5. **2번을 수행할때 미리 각 값이 in order list의 몇번째에 있는지 구해놓기
"""
from sys import stdin, setrecursionlimit

def f(inorder_lp: int, inorder_rp: int, postorder_lp: int, postorder_rp: int):
    global answer, inorder, postorder, inorder_index
    if inorder_rp-inorder_lp and postorder_rp-postorder_lp:
        root_value = postorder[postorder_rp-1]
        root_index = inorder_index[root_value]
        answer.append(root_value)

        left_inorder_lp, left_inorder_rp = inorder_lp, root_index
        left_postorder_lp, left_postorder_rp = postorder_lp, postorder_lp+root_index-inorder_lp
        f(left_inorder_lp, left_inorder_rp, left_postorder_lp, left_postorder_rp)

        right_inorder_lp, right_inorder_rp = root_index+1, inorder_rp
        right_postorder_lp, right_postorder_rp = left_postorder_rp, postorder_rp-1
        f(right_inorder_lp, right_inorder_rp, right_postorder_lp, right_postorder_rp)

setrecursionlimit(10**6)
stdin.readline()
inorder = [*map(int, stdin.readline().split())]
postorder = [*map(int, stdin.readline().split())]
inorder_index = {}
for i, v in enumerate(inorder):
    inorder_index[v] = i
answer = []

f(0, len(inorder), 0, len(postorder))
print(*answer)











"""
백준 1068 트리 (골드5)

1. 주어진 부모 정보를 통해 특정 노드의 자식을 저장하는 리스트 생성
2. 1 과정을 진행할때 제외할 노드는 리스트에 추가하지 않음
3. root node에서부터 BFS 시작
   => 제외할 노드부분은 끊겨 있을 것이므로 알아서 제외됨
4. 자식이 없는 노드(리프)는 answer에 count

** 주의할 점으로 루트노드를 제외하고 BFS를 돌리면 1개가 카운트되므로,
   이 부분만 예외처리로 0을 리턴하게 만듦
"""
from sys import stdin
from collections import deque

N = int(stdin.readline())
parents = [*map(int, stdin.readline().split())]
childs = [set() for _ in range(N)]
x_node = int(stdin.readline())
root_node = 0
for child in range(N):
    parent = parents[child]
    if parent!=-1:
        if child!=x_node and parent!=x_node:
            childs[parent].add(child)
    else:
        root_node = child
if root_node==x_node:
    print(0)
    exit()
answer = 0
q = deque([(root_node)])
while q:
    node = q.popleft()
    if childs[node]:
        for next_node in childs[node]:
            q.append(next_node)
    else:
        answer += 1
print(answer)




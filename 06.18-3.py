"""
백준 2533 사회망 서비스(SNS)

1. 재귀함수 구현 -> 특정 노드를 입력하면 해당 노드를 루트로하는 서브트리의
   최소 얼리어답터의 수를 알려주는 함수
2. 단, root node가 얼리어답터인지 여부에 따라 값이 달라질 수 있기 때문에
   [root가 얼리어답터 인경우, 아닌경우 두가지 답을 return하도록 구성
3-1. root가 얼리어답터가 아닌 경우 하위 모든 노드의 재귀함수를 돌리고
     각 결과값의 첫번째값(하위 노드가 얼리어답터인 경우)만을 가져와 더해줌
3-2. root가 얼리어답터인 경우 하위 모든 노드의 재귀함수를 돌리고
     각 결과값중 작은값만을 가져와 더해줌
"""
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
N = int(stdin.readline())
links = [set() for _ in range(N+1)]
for i in stdin:
    fr, to = map(int, i.split())
    links[fr].add(to)
    links[to].add(fr)

def f(node: int) -> list:
    global visited
    result = [1, 0]
    for next_node in links[node]:
        if not visited[next_node]:
            visited[next_node] = 1
            early, not_early = f(next_node)
            result[0] += min(early, not_early) 
            result[1] += early
    return result

visited = [0]*(N+1)
visited[1] = 1

print(min(f(1)))
"""
백준 4195 친구 네트워크 (골드2)

** union-find 유형에서 설정 3가지가 추가된 문제
   1. 보통 node는 int로 주어지는데, 여기선 string(이름)으로 주어짐
      => name_dict를 운영해 각 노드를 int로 변환

   2. 각 집합에 속하는 node 수를 구해야함
      => cnt_dict를 운영해 union 함수가 실행될때마다 집합원 수를 업데이트

   3. node의 수가 초기에 정해져있지 않음(동적임)
      => name_dict를 통해 새로운 노드가 추가될때마다 parents 리스트를 갱신
"""
from sys import stdin

def find(x: int) -> int:
    global parents
    if x!=parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(a: int, b: int):
    global parents, cnt_dict
    ra, rb = find(a), find(b)
    if ra!=rb:
        parents[max(ra, rb)] = min(ra, rb)
        cnt_dict[min(ra, rb)] += cnt_dict[max(ra, rb)]

input = stdin.readline

for _ in range(int(input())):
    N = int(input())
    parents = []
    name_dict = {}
    cnt_dict = {}
    idx = 0
    for __ in range(N):
        n1, n2 = input().strip().split()
        for name in [n1, n2]:
            if name not in name_dict:
                name_dict[name] = idx
                cnt_dict[idx] = 1
                parents.append(idx)
                idx += 1
        idx1, idx2 = name_dict[n1], name_dict[n2]
        union(idx1, idx2)
        print(cnt_dict[find(idx1)])
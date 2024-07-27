"""
백준 4195 친구 네트워크 (골드2)

민혁이는 소셜 네트워크 사이트에서 친구를 만드는 것을 좋아하는 친구이다. 
우표를 모으는 취미가 있듯이, 민혁이는 소셜 네트워크 사이트에서 친구를 모으는 것이 취미이다.

어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.

친구 네트워크란 친구 관계만으로 이동할 수 있는 사이를 말한다.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스의 첫째 줄에는 친구 관계의 수 F가 주어지며, 이 값은 100,000을 넘지 않는다. 
다음 F개의 줄에는 친구 관계가 생긴 순서대로 주어진다. 친구 관계는 두 사용자의 아이디로 이루어져 있으며, 알파벳 대문자 또는 소문자로만 이루어진 길이 20 이하의 문자열이다.

출력
친구 관계가 생길 때마다, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.

예제 입력 1 
2
3
Fred Barney
Barney Betty
Betty Wilma
3
Fred Barney
Betty Wilma
Barney Betty
예제 출력 1 
2
3
4
2
2
4
"""
from sys import stdin

def find(x: int) -> int:
    global parents
    if x!=parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(a: int, b: int):
    global parents
    ra, rb = find(a), find(b)
    if ra!=rb:
        parents[max(ra, rb)] = min(ra, rb)

input = stdin.readline

for _ in range(int(input())):
    N = int(input())
    name_dict = {}
    parents = []
    dp_dict = {}
    idx = 0
    for __ in range(N):
        n1, n2 = input().strip().split()
        # 두 이름이 이미 친구리스트에 있는경우
        if n1 in name_dict and n2 in name_dict:
            idx1, idx2 = name_dict[n1], name_dict[n2]
            ra, rb = find(idx1), find(idx2)
            if ra!=rb:
                dp_dict[min(ra, rb)] += dp_dict[max(ra, rb)]
            union(idx1, idx2)
            print(dp_dict[min(ra, rb)])
            continue
        # 한 이름이라도 새로 추가된 경우
        for name in [n1, n2]:
            if name not in name_dict:
                name_dict[name] = idx
                parents.append(idx)
                idx += 1
        idx1, idx2 = name_dict[n1], name_dict[n2]
        union(idx1, idx2)
        root = find(idx1)
        if root not in dp_dict:
            dp_dict[root] = 2
        else:
            dp_dict[root] += 1
        print(dp_dict[root])
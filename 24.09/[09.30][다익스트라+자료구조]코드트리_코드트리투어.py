"""
코드트리 코드트리 투어

1. 다익스트라로 노드까지의 최단거리 구해야함
**1-1. 500 커맨드 때문에 각 노드에서 모든 노드까지의 최단거리 table을 만들었으나,
       이렇게 하면 시간초과남 => 500 커맨드가 최대 15번만 나오기 때문임.
2. 조건에 맞게 각종 자료구조를 사용해 여행 코스와 최소 비용 여행을 찾아야함
3. 새 코스 추가/제거 해야하므로 hash 자료구조(dict) 활용
4. 가장 수익이 큰 코스를 뽑아내야하므로 heap 활용
"""
from sys import stdin
from heapq import heappop, heappush

# start_node로부터의 최단거리 갱신
def make_cost_table(start_node: int):
    global costs, links, N
    costs = [float("inf")]*N
    costs[start_node] = 0
    hq = [(0, start_node)]
    while hq:
        cost, node = heappop(hq)
        for new_node, new_cost in links[node]:
            if cost+new_cost<costs[new_node]:
                costs[new_node] = cost+new_cost
                heappush(hq, (cost+new_cost, new_node))

# 노드간 연결 정리
stdin.readline()
lst = [*map(int, stdin.readline().split())]
N, _ = lst[1], lst[2]
links = [set() for _ in range(N)]
for i in range(3, len(lst), 3):
    fr, to, weight = lst[i:i+3]
    links[fr].add((to, weight))
    links[to].add((fr, weight))

# 0으로부터의 최단거리 정리
costs = [float("inf")]*N
make_cost_table(0)

# 조건에 맞게 수행
courses = {}
hq = []
start_node = 0
for i in stdin:
    lst = [*map(int, i.split())]
    if lst[0]==200:
        # 새 코스가 추가되면 courses에 추가
        # 동시에 수익이 +라면 heap에 추가 
        id, revenue, dest = lst[1:]
        if revenue>=costs[dest]:
            heappush(hq, (costs[dest]-revenue, id))
        courses[id] = (revenue, dest)
    elif lst[0]==300:
        # 없앨 id가 코스에 있다면 삭제
        if lst[1] in courses:
            del courses[lst[1]]
    elif lst[0]==400:
        # hq로 수익이 가장 큰 코스 뽑기
        # 뽑은 코스가 300에 의해 제외되었다면 다음 코스 뽑기
        while hq:
            cost, id = heappop(hq)
            if id in courses:
                del courses[id]
                print(id)
                break
        else:
            print(-1)
    else:
        # 시작 노드가 바뀌었으므로 각 노드까지의 최단거리 갱신
        # heap 새롭게 생성
        start_node = lst[1]
        make_cost_table(start_node)
        new_hq = []
        for id, (revenue, dest) in courses.items():
            if revenue>=costs[dest]:
                heappush(new_hq, (costs[dest]-revenue, id))
        hq = new_hq
"""
백준 2568 전깃줄 - 2 (플래티넘5)

1. 전기줄 1 문제와 매커니즘이 비슷함
2. 첫번째 젓기줄부터 순서대로 for문을 진행
3. 반대쪽에 이어진 node번호를 to라고 할때, to와 to 이하 바르게 이어질 수 있는
   전기줄의 최대 개수를 tuple 형태로 저장
4. to의 크기를 바탕으로 이분탐색을 활용해 lst에서의 위치를 찾아냄
5. 찾아낸 위치의 왼쪽값+1 만큼을 lst에 추가함
6. 단, 왼쪽값+1과 똑같은 값이 있다면 해당 값을 갱신
7. 맨 처음 있었던 전기줄 node set에서 최대 전기줄 조합에서의 node set의
   차집합을 구해 이어진 node만을 출력함
"""
from sys import stdin
from bisect import bisect_left

N = int(stdin.readline())
lst = []
fr_set = set()
for i in stdin:
    fr, to = map(int, i.split())
    lst.append((fr, to))
    fr_set.add(fr)
lst.sort()
bisect_lst = []
for fr, to in lst:
    if bisect_lst:
        idx = bisect_left(bisect_lst, (to, 1, set()))
        if idx==len(bisect_lst):
            _, left_cnt, left_visited = bisect_lst[idx-1]
        else:
            right_to, right_cnt, _ = bisect_lst[idx]
            if idx==0:
                left_cnt, left_visited = 0, set()
            else:
                _, left_cnt, left_visited = bisect_lst[idx-1]
            if right_cnt==left_cnt+1:
                temp = left_visited.copy()
                temp.add(fr)
                bisect_lst[idx] = (to, left_cnt+1, temp)
                continue
        temp = left_visited.copy()
        temp.add(fr)
        bisect_lst.insert(idx, (to, left_cnt+1, temp))
    else:
        bisect_lst.append((to, 1, {fr}))

answer = sorted(fr_set-bisect_lst[-1][-1]) 
print(len(answer))
print(*answer)



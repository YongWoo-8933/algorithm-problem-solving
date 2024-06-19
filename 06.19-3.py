"""
백준 2568 전깃줄 - 2

두 전봇대 A와 B 사이에 하나 둘씩 전깃줄을 추가하다 보니 전깃줄이 서로 교차하는 경우가 발생하였다. 
합선의 위험이 있어 이들 중 몇 개의 전깃줄을 없애 전깃줄이 교차하지 않도록 만들려고 한다.

예를 들어, <그림 1>과 같이 전깃줄이 연결되어 있는 경우 
A의 1번 위치와 B의 8번 위치를 잇는 전깃줄, 
A의 3번 위치와 B의 9번 위치를 잇는 전깃줄, 
A의 4번 위치와 B의 1번 위치를 잇는 전깃줄을 
없애면 남아있는 모든 전깃줄이 서로 교차하지 않게 된다. 

<그림 1>

전깃줄이 전봇대에 연결되는 위치는 전봇대 위에서부터 차례대로 번호가 매겨진다. 
전깃줄의 개수와 전깃줄들이 두 전봇대에 연결되는 위치의 번호가 주어질 때, 
남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 
최소 개수의 전깃줄을 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 두 전봇대 사이의 전깃줄의 개수가 주어진다. 전깃줄의 개수는 100,000 이하의 자연수이다. 
둘째 줄부터 한 줄에 하나씩 전깃줄이 A전봇대와 연결되는 위치의 번호와 B전봇대와 연결되는 위치의 번호가 차례로 주어진다. 
위치의 번호는 500,000 이하의 자연수이고, 같은 위치에 두 개 이상의 전깃줄이 연결될 수 없다. 

출력
첫째 줄에 남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 출력한다. 
둘째 줄부터 한 줄에 하나씩 없애야 하는 전깃줄의 A전봇대에 연결되는 위치의 번호를 오름차순으로 출력한다. 
만약 답이 두 가지 이상이라면 그 중 하나를 출력한다.

예제 입력 1 
8
1 8
3 9
2 2
4 1
6 4
10 10
9 7
7 6
예제 출력 1 
3
1
3
4

9
1 50000
2 4
3 11
4 12
5 6
6 3
7 2
8 9
9 10

answer:
5
1
3
4
6
7
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



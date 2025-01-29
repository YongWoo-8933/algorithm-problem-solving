"""
백준 31804 Chance! (골드4)

1. 도착점수에서 출발점수로 가는게 이득임(자연수 성질 활용)
2. BFS로 방문 체크하면서 이동동
"""
from collections import deque

def main():
    a, b = map(int, input().split())
    q = deque([(b, 1, 0)])
    visited = [False]*(b+1)
    visited[b] = True
    while q:
        x, chance_cnt, magic_cnt = q.popleft()
        if x==a:
            print(magic_cnt)
            exit()
        if x%10==0 and chance_cnt>0 and x//10>=a and not visited[x//10]:
            visited[x//10] = True
            q.append((x//10, 0, magic_cnt+1))
        if x%2==0 and x//2>=a and not visited[x//2]:
            visited[x//2] = True
            q.append((x//2, chance_cnt, magic_cnt+1))
        if not visited[x-1]:
            visited[x-1] = True
            q.append((x-1, chance_cnt, magic_cnt+1))

main()
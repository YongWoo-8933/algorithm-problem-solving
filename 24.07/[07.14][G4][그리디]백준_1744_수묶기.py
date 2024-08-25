"""
백준 1744 수 묶기 (골드4)

1. 1보다 큰 양수들은 큰 순서대로 짝지어 더해줌
2. 1은 다른수와 곱하면 더한것보다 작아지므로 그냥 더해만 줌
3. 음수도 절댓값 큰 순으로 짝지어 곱해줌
4. 짝을 이루지 못한 음수가 있다면 0과 곱해주고, 0도 없다면 그냥 더해줌 
"""
from sys import stdin

N = int(stdin.readline())
lst = [*map(int, stdin)]
lst.sort()
p = N-2
answer = 0
while p>=0 and lst[p]>1:
    answer += lst[p]*lst[p+1]
    p -= 2
if p+1>=0 and lst[p+1]>1:
    answer += lst[p+1]
answer += lst.count(1)
p = 1
while p<N and lst[p]<=0:
    answer += lst[p-1]*lst[p]
    p += 2
if p-1<N and lst[p-1]<0:
    answer += lst[p-1]
print(answer)

"""
백준 2166 다각형의 면적 (골드5)

1. 신발끈공식(외적을 활용한 도형넓이 구하기) 그냥 적용
"""
from sys import stdin

N = int(stdin.readline())
points = [[*map(int, i.split())] for i in stdin]
v = sum(points[i][0]*points[i+1][1]-points[i+1][0]*points[i][1] for i in range(N-1))
v += points[N-1][0]*points[0][1]-points[0][0]*points[N-1][1]
area = 0.5*abs(v)
print(int(area*10+0.5)*0.1)




    


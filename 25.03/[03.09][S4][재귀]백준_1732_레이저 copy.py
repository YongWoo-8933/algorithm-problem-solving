"""
백준 1732 레이저 (골드2)

1. 나중에 잘하는 사람한테 물어보기
"""
from math import gcd
from sys import stdin

def main():
    stdin.readline()
    categorized_coords = dict()
    is_zero_exist = False
    zero_z = 0
    for i in stdin:
        x, y, z = map(int, i.split())
        if x==0 and y==0:
            is_zero_exist = True
            zero_z = z
            continue
        gcd_xy = gcd(x, y)
        a = (x//gcd_xy, y//gcd_xy)
        if a in categorized_coords:
            categorized_coords[a].append((x, y, z))
        else:
            categorized_coords[a] = [(x, y, z)]
    answer = []
    for coords in categorized_coords.values():
        height = 0
        if is_zero_exist:
            coords.append((0, 0, zero_z))
        for x, y, z in sorted(coords, key=lambda k: abs(k[0])):
            if z<=height:
                answer.append((x, y))
            else:
                height = z
    answer.sort()
    for x, y in answer:
        print(x, y)

main()
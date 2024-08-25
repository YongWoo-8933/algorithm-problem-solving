"""
백준 17387 선분 교차 2 (골드2)

** ccw알고리즘 공부 반드시 필요함
1. ccw 알고리즘으로 크게 두 직선의 기울기가 같을때와 다를때로 나눔
2. 기울기가 같을때는 x축에 수직인지 여부를 구분해 겹치는 부분이 있는지 판정
3. 기울기가 다르면 ccw값의 곱이 음수인지 판정
"""

def ccw(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> int:
    return  x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

ccw1, ccw2 = ccw(x1, y1, x2, y2, x3, y3), ccw(x1, y1, x2, y2, x4, y4)
ccw3, ccw4 = ccw(x3, y3, x4, y4, x1, y1), ccw(x3, y3, x4, y4, x2, y2)

if ccw1*ccw2==0 and ccw3*ccw4==0:
    if x1==x2:
        # 수직 선분
        if min(y1, y2)>max(y3, y4) or min(y3, y4)>max(y1, y2):
            print(0)
        else:
            print(1)
    else:
        # 그 외 선분
        if min(x1, x2)>max(x3, x4) or min(x3, x4)>max(x1, x2):
            print(0)
        else:
            print(1)
elif ccw1*ccw2==0:
    print([0, 1][ccw3*ccw4<0])
elif ccw3*ccw4==0:
    print([0, 1][ccw1*ccw2<0])
else:
    print([0, 1][ccw3*ccw4<0 and ccw1*ccw2<0])



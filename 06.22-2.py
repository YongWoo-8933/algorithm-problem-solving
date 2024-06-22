"""
백준 16434 드래곤 앤 던전

1. 시작 Hp를 0으로 두고, 포션회복을 해도 Hp가 0이상 올라갈 수 없다고 하자.
2. 해당 조건을 유지하면서 방을 모두 돌았을 때 가장 hp가 낮게 내려간 순간을 기록.
3. 가장 낮았던 hp값보다 1 높게 hp 설정하면 됨.
"""
from sys import stdin

N, HATK = map(int, stdin.readline().split())
cur_hp, min_hp = 0, 0

for i in stdin:
    ti, ai, hi = map(int, i.split())
    if ti==1:
        monster_attack_num = (hi-1)//HATK
        cur_hp -= ai*monster_attack_num
        min_hp = min(min_hp, cur_hp)
    elif ti==2:
        cur_hp += hi
        HATK += ai
        if cur_hp>0: cur_hp=0

print(-min_hp+1)
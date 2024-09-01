"""
백준 15787 기차가 어둠을 헤치고 은하수를 (실버2)

1. 비트마스킹으로 기차 상태를 기록
2. 명령이 끝나면 set으로 만들어 중복을 없애고 기차수를 return
"""
from sys import stdin

def main():
    N, M = map(int, stdin.readline().split())
    limit = 2**20
    trains = [0]*(N+1)
    for i in stdin:
        if i[0]=="1":
            _, train, seat = map(int, i.split())
            trains[train] = trains[train] | (1<<(seat-1))
        elif i[0]=="2":
            _, train, seat = map(int, i.split())
            trains[train] = trains[train] & ~(1<<(seat-1))
        elif i[0]=="3":
            _, train = map(int, i.split())
            trains[train] = trains[train]<<1
            trains[train] %= limit
        elif i[0]=="4":
            _, train = map(int, i.split())
            trains[train] = trains[train]>>1
    print(len(set(trains[1:])))
    
main()
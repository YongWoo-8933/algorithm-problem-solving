"""
백준 1700 멀티탭 스케줄링 (골드1)

** 코어 아이디어: 다음에 등장할 디바이스들은 최대한 멀티탭에 남겨둬야 함.
                 따라서 현재 멀티탭에 꽂혀있는 기기들 중 가장 마지막에 등장할
                 하나의 기기를 찾아 뽑아내면 됨
1. multitap이라는 set을 운영해 현재 꽂혀있는 디바이스면 패스
2. 꽂혀있지 않다면 이후 꽂힐 디바이스를 체크하며 가장 마지막에 쓰이거나
   안쓰이는 기기를 찾아 뽑아냄
"""

def main():
    N, K = map(int, input().split())
    devices = [*map(int, input().split())]
    multitap = set()
    answer = 0
    for i in range(K):
        device = devices[i]
        if device not in multitap and len(multitap)>=N:
            answer += 1
            temp_multitap = multitap.copy()
            j = i+1
            while len(temp_multitap)>1 and j<K:
                next_device = devices[j]
                if next_device in temp_multitap:
                    temp_multitap.remove(next_device)
                j += 1
            pop_device = temp_multitap.pop()
            multitap.remove(pop_device)
        multitap.add(device)
    print(answer)
main()
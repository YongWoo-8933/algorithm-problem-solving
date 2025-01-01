"""
백준 1495 기타리스트 (실버1)

1. 브루트포스로 다음에 나올 수 있는 모든 볼륨을 순회
"""

def main():
    _, S, M = map(int, input().split())
    volumns = [*map(int, input().split())]
    dp = {S}
    for volumn in volumns:
        new_dp = set()
        for m in dp:
            for new_m in [m+volumn, m-volumn]:
                if 0<=new_m<=M:
                    new_dp.add(new_m)
        if not new_dp:
            print(-1)
            exit()
        dp = new_dp
    print(max(dp))
        
main()
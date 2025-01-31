"""
백준 20300 서강근육맨 (실버3)

1. 두 기구를 짝지었을 때 피로도가 최대한 작아져야함.
2. 이를 위해 큰 피로도의 기구는 최대한 작은 피로도의 기구와 연결.
"""
def main():
    N = int(input())
    lst = [*map(int, input().split())]
    if N%2!=0:
        lst.append(0)
        N += 1
    lst.sort()
    answer = 0
    for i in range(N//2):
        answer = max(answer, lst[i]+lst[N-i-1])
    print(answer)

main()
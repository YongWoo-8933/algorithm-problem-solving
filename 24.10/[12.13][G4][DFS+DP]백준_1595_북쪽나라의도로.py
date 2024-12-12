"""
백준 1595 북쪽나라의도로(골드4)

* 오른쪽, 아래쪽으로만 이동 가능하다면 FS 시리즈가 아니라 DP로 가야한다
1. DP로 갈 수 있는곳만 카운트
"""
from sys import stdin

def main():
    N = 1
    temp = []
    for i in stdin:
        fr, to, dist = map(int, i.split())
        N = max(N, fr, to)
        temp.append((fr, to, dist))
    links = [set() for _ in range(N+1)]
    for fr, to, dist in temp:
        links[fr].add((to, dist))
        links[to].add((fr, dist))
    dp = [dict() for _ in range(N+1)]

    def dfs(fr: int, node: int) -> int:
        result = 0
        for to, dist in links[node]:
            if to!=fr:
                if to not in dp[node]:
                    dp[node][to] = dfs(node, to)+dist
                result = max(result, dp[node][to])
        return result        

    answer = 0
    for node in [i for i in range(1, N+1) if len(links[i])==1]:
        answer = max(answer, dfs(0, node))
    
    print(answer)

main()

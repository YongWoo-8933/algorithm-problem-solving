"""
백준 1562 계단수 (골드1)

1. DP + 비트마스킹으로 풀리는 문제(매우 어려운편, 풀이 참고함)
(https://konkukcodekat.tistory.com/139)
2. 다만, 위 풀이와 달리 굳이 dp 테이블에 자릿수 정보를 저장할 필요가 없어보여 생략
3. 1023개의 모든 칸을 만들고 1023번 for문을 돌리자니 쓸데없는 방문이 많아짐.
   따라서 dict를 구현해 갯수가 0인(방문하지 않아도 되는) 경우는 for문에 넣지 않음
"""
def main():
    N = int(input())
    dp = [dict() for _ in range(10)]
    for e in range(1, 10):
        dp[e][(1<<e)] = 1
    for _ in range(N-1):
        new_dp = [dict() for _ in range(10)]
        for e in range(10):
            for bits, cnt in dp[e].items():
                for next_e in [e+1, e-1]:
                    if 0<=next_e<10:
                        new_bits = bits|(1<<next_e)
                        if new_bits in new_dp[next_e]:
                            new_dp[next_e][new_bits] += cnt
                        else:
                            new_dp[next_e][new_bits] = cnt
                        new_dp[next_e][new_bits] %= 1000000000
        dp = new_dp
    answer = 0
    for e in range(10):
        if 1023 in dp[e]:
            answer += dp[e][1023]
    print(answer%1000000000)
main()
"""
백준 1806 부분합 

풀이1 - dp풀이
1. 누적합 dp와 min_length, answer 세 변수를 설정
2. 수열의 순서대로 for문을 도는데, 각 회차마다 dp에 합을 누적시키고 min_lenght값을 1씩 증가
3. 만약 해당 회차에 누적합 dp값이 S보다 커졌다면, 누적합이 S보다 큰 조건 하에서 min_length를 1씩 줄여봄
4. 더이상 min_length를 줄일 수 없으면(더 줄일경우 dp가 S보다 작아지는 임계점) 해당 min_lenght에서 answer 갱신
5. 위 과정 반복

풀이2 - two pointer풀이
1. 수열합의 범위를 지정할 좌우 포인터 lp, rp와 수열합 sequence_sum을 0, 0, 0으로 설정
2. sequence_sum이 S보다 작으면 sequence[rp]값은 수열합에 더하고 rp를 오른쪽으로 이동
3. sequence_sum이 S보다 커지면 answer를 갱신하고 수열합에서 sequence[lp]값을 뺀 뒤 lp를 오른쪽으로 이동
4. lp가 rp보다 커지거나 rp가 범위를 벗어나면 종료
"""
N, S = map(int, input().split())
sequence = [*map(int, input().split())]
answer = float("inf")

# 풀이1
min_length = 0
dp = 0
for i in range(N):
    dp += sequence[i]
    min_length += 1
    if dp >= S:
        s = sequence[i-min_length+1]
        while dp-s>=S:
            dp -= s
            min_length -= 1
            s = sequence[i-min_length+1]
        answer = min(answer, min_length)
print(answer if answer!=float("inf") else 0)

# 풀이2
lp, rp = 0, 0
sequence_sum = 0
while lp<=rp:
    if sequence_sum<S and rp<N:
        sequence_sum += sequence[rp]
        rp += 1
    elif sequence_sum>=S:
        answer = min(answer, rp-lp)
        sequence_sum -= sequence[lp]
        lp += 1
    else:
        break
print(answer if answer!=float("inf") else 0)
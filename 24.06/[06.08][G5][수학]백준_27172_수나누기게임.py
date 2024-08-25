"""
백준 27172 수 나누기 게임 (골드5)

1. 에라토스테네스의 체 원리와 비슷하게 풀이 진행
2. card중 최대값을 찾아 이 값과 길이가 같은 scores라는 배열을 만들어 None으로 초기화
3. 주어진 카드를 순회하며 scores[card값]의 원소를 0으로 초기화
4. 다시 카드를 순회하는데, 값을 2/3/4..씩 곱해가며 배수에 해당하는 카드가 존재하면 -1점씩, 본인은 +1점씩 가져감
5. 배수 계산은 카드의 max값까지만 진행
"""
input()
cards = [*map(int, input().split())]
max_card = max(cards)
scores = [None]*(max_card+1)
for card in cards:
    scores[card] = 0
for card in cards:
    i = 2
    while card*i<=max_card:
        if scores[card*i] is not None:
            scores[card*i] -= 1
            scores[card] += 1
        i+=1
print(*[scores[card] for card in cards])










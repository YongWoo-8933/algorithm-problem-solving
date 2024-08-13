"""
백준 9328 열쇠

1. MAP과 key설정
2. entrances 배열을 운영 > entrances에는 탐색하며 만난 문(대문자) 좌표, 가장자리에서 진입 가능한 경우 추가
3. 매 순회마다 entrances에서 진입가능한(문일 경우 key가 존재할경우) 좌표를 q에 추가
4. q가 비어있을경우(진입 가능한 좌표가 하나도 없는경우) 종료
5. q가 있을 경우 해당 시작점에서 BFS 진행
"""
from sys import stdin
from collections import deque

input = stdin.readline

for _ in range(int(input())):
    H, W = map(int, input().split())
    MAP = [[*input().strip()] for _ in range(H)]
    keys = {"."}
    for i in input().strip():
        if i!="0":
            keys.add(i.upper())

    # 입구 찾기 -> 가장자리가 . / $ / key / door 인경우 entrances에 추가
    # $는 "."으로 바꾸고 answer +1
    # key는 "."으로 바꾸고 keys에 추가
    answer = 0
    entrances = set()
    for row in range(H):
        columns = range(W) if row in [0, H-1] else [0, W-1]
        for col in columns:
            x = MAP[row][col]
            if x=="*":
                continue
            elif x=="$":
                answer += 1
                MAP[row][col] = "."
                entrances.add((row, col))
            elif x==".":
                entrances.add((row, col))
            elif x.islower():
                keys.add(x.upper())
                MAP[row][col] = "."
                entrances.add((row, col))
            elif x.isupper():
                entrances.add((row, col))
    
    # 탐색 > 모든 입구를 돌아다니면서 key는 수집
    #      > door를 만나면 entrances에 추가
    #      > $를 만나면 "."으로 바꾸고 answer 추가
    visited = [[0]*W for _ in range(H)]
    while 1:
        q = deque()
        # entrances를 순회하며 방문하지 않은 entrance는 q에 추가
        # 문을 만났는데 key가 있으면 q에 추가
        for s_row, s_col in entrances:
            x = MAP[s_row][s_col]
            if not visited[s_row][s_col] and x in keys:
                visited[s_row][s_col] = 1
                q.append((s_row, s_col))
        # 탐색 가능한 좌표가 하나도 없을경우 break
        if not q:
            break
        while q:
            row, col = q.popleft()
            for dx, dy in zip([0, 0, -1, 1], [1, -1, 0, 0]):
                n_row, n_col = row+dy, col+dx
                if 0<=n_row<H and 0<=n_col<W and not visited[n_row][n_col]:
                    x = MAP[n_row][n_col]
                    if x=="*":
                        visited[n_row][n_col] = 1
                    elif x=="$":
                        q.append((n_row, n_col))
                        visited[n_row][n_col] = 1
                        answer += 1
                    elif x==".":
                        q.append((n_row, n_col))
                        visited[n_row][n_col] = 1
                    elif x.isupper():
                        entrances.add((n_row, n_col))
                    elif x.islower():
                        keys.add(x.upper())
                        visited[n_row][n_col] = 1
                        q.append((n_row, n_col))
    
    print(answer)








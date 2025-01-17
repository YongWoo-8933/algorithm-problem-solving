"""
백준 15559 내 선물을 받아줘 (골드2)

1. union-find로 같은 loop안에있는 칸을 분류 -> 2차원 노드들을 1차원으로 펴서 저장
2. 각 칸을 순회하며 방문 체크 후 union 진행
3. 집합의 갯수 count
"""

from sys import stdin

def main():
    H, W = map(int, stdin.readline().split())
    MAP = [i.strip() for i in stdin]
    roots = [i for i in range(H*W)]

    def find(x: int) -> int:
        if roots[x]!=x:
            roots[x] = find(roots[x])
        return roots[x]

    def union(a: int, b: int):
        ra, rb = roots[a], roots[b]
        if ra!=rb:
            roots[max(ra, rb)] = min(ra, rb)

    visited = [[False]*W for _ in range(H)]
    for row in range(H):
        for col in range(W):
            if not visited[row][col]:
                visited[row][col] = True
                r, c = row, col
                while True:
                    if MAP[r][c]=="N":
                        nr, nc = r-1, c
                    elif MAP[r][c]=="E":
                        nr, nc = r, c+1
                    elif MAP[r][c]=="S":
                        nr, nc = r+1, c
                    else:
                        nr, nc = r, c-1
                    if 0<=nr<H and 0<=nc<W:
                        if not visited[nr][nc]:
                            visited[nr][nc] = True
                            union(r*W+c, nr*W+nc)
                            r, c = nr, nc
                            continue
                        else:
                            union(r*W+c, nr*W+nc)
                    break
    
    answer = set()
    for i in range(H*W):
        answer.add(find(i))
    print(len(answer))

main()
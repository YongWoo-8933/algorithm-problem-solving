"""
백준 16235 나무 재테크 (골드3)

# 1차 시도
1. 나무 정보와 영양분 정보를 N*N*(각 칸의 나무갯수) 배열에 저장
2. 계절 조건에 맞게 하드코딩 후 K년 진행

==> pypy3에서는 통과하지만 python3에서는 어떤 방법을 써도 시간초과
==> 맞힌 사람들의 실행시간을 보니 시간을 줄일 무언가가 필요해보임


# 2차 시도
1. 나무 정보와 영양분 정보를 N*N*(각 칸의 나무갯수) 배열에 저장
   ** 단, 각 칸에 리스트를 만드는게 아니라 dictionary를 만들고,
   ** 'age : 해당 나이 나무의 갯수'로 저장함
   ** 이로써 같은 나이의 나무에 대한 반복 중복연산 제거
2. 봄에 양분을 먹을 때, 나이순으로 양분을 먹기때문에 
   땅에 양분이 모자라는 시점 이후로는 모든 나무가 양분이 될것임.
   이를 고려해 모든 나무가 for문으로 돌아가는게 아닌 해당 시점이후로는
   모두 양분처리함으로써 최악 시간복잡도를 줄이는게 포인트
3. 가을에 인접 칸에 번식을 진행할때는 dict의 이점을 살려 5의 배수나이 나무 갯수만큼 번식

==> 몇가지 아이디어를 추가하니 시간초과 극복
"""
from sys import stdin

# 봄+여름 - 양분먹기/죽기 + 죽은나무 양분화
def spring_summer():
    global N, trees, field
    for row in range(N):
        for col in range(N):
            if trees[row][col]:
                new_trees = {}
                dead_trees = 0
                for age in sorted(trees[row][col]):
                    needs = age*trees[row][col][age]
                    if field[row][col]>=needs:
                        field[row][col] -= needs
                        if age+1 in new_trees:
                            new_trees[age+1] += trees[row][col][age]
                        else:
                            new_trees[age+1] = trees[row][col][age]
                    else:
                        Q = field[row][col]//age
                        if Q:
                            field[row][col] -= Q*age
                            if age+1 in new_trees:
                                new_trees[age+1] += Q
                            else:
                                new_trees[age+1] = Q
                            dead_trees += (age//2)*(trees[row][col][age]-Q)
                        else:
                            dead_trees += (age//2)*trees[row][col][age]
                trees[row][col] = new_trees
                field[row][col] += dead_trees

# 가을 - 인접 8칸 번식
def fall():
    global N, trees
    new_trees = {}
    for r in range(N):
        for c in range(N):
            for age in trees[r][c].keys():
                if age%5==0:
                    for row, col in [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]:
                        if 0<=row<N and 0<=col<N:
                            if (row, col) in new_trees:
                                new_trees[(row, col)] += trees[r][c][age]
                            else:
                                new_trees[(row, col)] = trees[r][c][age]
    for (row, col), cnt in new_trees.items():
        if 1 in trees[row][col]:
            trees[row][col][1] += cnt
        else:
            trees[row][col][1] = cnt
    

# 겨울 - 필드에 양분추가
def winter():
    global N, A, field
    for row in range(N):
        for col in range(N):
            field[row][col] += A[row][col]

input = stdin.readline
N, M, K = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]
trees = [[{} for _ in range(N)] for __ in range(N)]
field = [[5]*N for _ in range(N)]
for i in stdin:
    r, c, age = map(int, i.split())
    if age in trees[r-1][c-1]:
        trees[r-1][c-1][age] += 1
    else:
        trees[r-1][c-1][age] = 1
for _ in range(K):
    spring_summer()
    fall()
    winter()
answer = 0
for row in range(N):
    for col in range(N):
        answer += sum(trees[row][col].values())
print(answer)
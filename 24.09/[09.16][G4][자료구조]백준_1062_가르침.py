"""
백준 1062 가르침 (골드 4)

1. 먼저 "a", "n", "t", "i", "c"는 반드시 읽어야하므로, K가 5보다 작으면 0 리턴
2. K가 5보다 큰 경우, 모든 단어를 순회하며 사용되는 알파벳 수집
3. 동시에 각 단어에서 사용되는 "a", "n", "t", "i", "c"를 제거한 나머지 필요 알파벳 정리
4. 모든 알파벳을 배울 수 있다면 모든 단어를 배움
5. 모든 알파벳을 배울 수 없다면, combination으로 (K-5)개 만큼 배우는 모든 조합을 구해
   각 조합에서 읽을 수 있는 단어의 수를 체크
6. 가장 읽을 수 있는 단어의 수가 많은 경우를 return
"""
from sys import stdin
from itertools import combinations

def main():
    _, K = map(int, stdin.readline().split())
    lst = [i.strip() for i in stdin]
    if K<5:
        print(0)
        return
    readable = {"a", "n", "t", "i", "c"}
    answer = 0
    word_sets = []
    alphabets = set()
    for word in lst:
        word_set = set(word)-readable
        if word_set:
            alphabets = alphabets.union(word_set)
            word_sets.append(word_set)
        else:
            answer += 1
    max_read = 0
    if len(alphabets)<=K-5:
        print(answer+len(word_sets))
    else:
        for comb in combinations(alphabets, K-5):
            readable = set(comb)
            cnt = 0
            for word_set in word_sets:
                if word_set<=readable:
                    cnt += 1
            max_read = max(max_read, cnt)
        print(answer+max_read)
main()
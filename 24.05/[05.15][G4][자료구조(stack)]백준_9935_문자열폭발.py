"""
백준 9935 문자열 폭발 (골드4)

1. stack에 문자열 추가
2. stack 마지막 부분에 폭발 문자열이 있다면 뽑아냄
"""
 
string, pattern = input(), [*input()]
len_pattern = len(pattern)
stack = []
for s in string:
    stack += s
    if s == pattern[-1]:
        while len(stack) >= len_pattern and stack[-len_pattern:] == pattern:
            del stack[-len_pattern:]
print("".join(stack) if stack else "FRULA")



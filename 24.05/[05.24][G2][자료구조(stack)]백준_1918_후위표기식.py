"""
백준 1918 후위 표기식 (골드2)

- 아래 조건에 맞게 구현 -
1. 피연산자는 그대로 출력
2. 연산자는 스택이 비어있으면 자신을 바로 추가
3. stack의 top이 자신보다 우선순위가 낮은 연산자를 만날 때까지 pop 하고 자신을 담음
4. 단, 여는 괄호는 닫는 괄호가 아니면 pop하지 않음
4. 닫는 괄호가 나오면 여는 괄호가 나올 때까지 꺼내서 출력
5. 마지막에 도착하면 스택에서 차례로 꺼내서 출력
"""
s = input()
stack = []
answer = ""
for chr in s:
    if ord("A") <= ord(chr) <= ord("Z"):
        answer += chr
    else:
        if stack:
            if chr == "(":
                stack.append(chr)
            elif chr == ")":
                while stack and stack[-1] != "(":
                    answer += stack.pop()
                stack.pop()
            elif chr in "*/":
                while stack and stack[-1] in "*/":
                    answer += stack.pop()
                stack.append(chr)
            elif chr in "+-":
                while stack and stack[-1] in "+-*/":
                    answer += stack.pop()
                stack.append(chr)
        else:
            stack.append(chr)
while stack:
    answer += stack.pop()
print(answer)


    


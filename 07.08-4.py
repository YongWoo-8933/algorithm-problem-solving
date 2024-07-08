"""
백준 2504 괄호의 값 (골드5)

1. 일반적인 괄호문제와 같이 stack으로 풀이 진행
2. (나 [가 나오면 stack에 추가하고, 
   )나 ]가 나오면 (나 [가 나올때까지 stack에서 pop
3. 위 과정이 원활하게 되지 않으면(stack이 비거있거나 맞지않은 쌍이 생기면) 종료
4. (나 [가 추가될때마다 depth를 한단계씩 늘려가며 해당 depth에서의 연산을 진행해
   같은 depth끼리의 값은 더해줌
5. 자신보다 한칸 깊은 depth의 값이 있으면 (X)나 [X]상황이므로
   2나 3을 곱해 해당 depth의 값에 더함
6. 마지막에 depth 0에 축적된 결과값을 출력
"""
stack = []
sum_values = []
depth_values = [0]*31
depth = 0
for s in input():
    if s in "([":
        depth += 1
        stack.append(s)
    elif s==")":
        if not stack or stack.pop()=="[":
            print(0)
            exit()
        depth -= 1
        next_depth_value = depth_values[depth+1] if depth_values[depth+1] else 1
        depth_values[depth] += 2*next_depth_value
        depth_values[depth+1] = 0
    elif s=="]":
        if not stack or stack.pop()=="(":
            print(0)
            exit()
        depth -= 1
        next_depth_value = depth_values[depth+1] if depth_values[depth+1] else 1
        depth_values[depth] += 3*next_depth_value
        depth_values[depth+1] = 0
print(depth_values[0])




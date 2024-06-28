"""
백준 17615 볼 모으기 (실버1)
** 실버1 치고는 꽤 생각하기 어려움

1. 공을 앞으로 빼는 경우와 뒤로 빼는 경우 모두 생각해줘야 함
2. 앞뒤로 빨간공을 뺄 때, 파란공을 뺄 때 빼야하는 공의 수를 세고
   가장 적은 경우를 찾아 리턴

"""
N = int(input())
balls = input()
answer = N
for temp_balls in [balls, balls[::-1]]:
    first_R_idx, first_B_idx = temp_balls.find("R"), temp_balls.find("B")
    if -1 in {first_R_idx, first_B_idx}:
        print(0)
        exit()
    if first_R_idx<first_B_idx:
        if first_B_idx+1<N:
            answer = min(answer, temp_balls[first_B_idx+1:].count("R"))
        else:
            print(0)
            exit()
        answer = min(answer, temp_balls[first_B_idx:].count("B"))
    else:
        if first_R_idx+1<N:
            answer = min(answer, temp_balls[first_R_idx+1:].count("B"))
        else:
            print(0)
            exit()
        answer = min(answer, temp_balls[first_R_idx:].count("R"))
print(answer)

"""
백준 14890 경사로 (골드3)

1. 각 라인을 체크하는 함수를 만들고(check_line)
2. 함수 내에서는 다음을 실행
    - 슬로프를 짓고 있는지 체크할 int형 변수 slope_remain은 남은 슬로프의 길이를 저장
    - 오르막길을 만날 경우 이전 경로에서 슬로프를 설치할 수 있었는지 체크하는 int형 margin 변수를 운영
    - 평지에서는 슬로프를 짓고있다면 마저 짓고 짓고있지 않다면 margin 길이 +1
    - 오르막길을 만나면 margin 체크하고 부족하면 False 리턴
    - 내리막길에서는 슬로프 짓고 있었다면 False 리턴
    - 내리막길인데 슬로프를 안짓고 있다면 짓기 시작
3. 2*N개의 라인에 대해 check_line 함수를 돌리고 True 갯수 리턴
"""
from sys import stdin

def check_line(line: list, l: int) -> bool:
    slope_remain, margin = l, 1
    for i in range(len(line)-1):
        p_height, height = line[i], line[i+1]
        # 두칸 이상 차이날 경우 실패
        if abs(p_height-height)>1:
            return False
        # 평지
        if p_height==height:
            # 슬로프 건설 진행중
            if slope_remain!=l:
                slope_remain -= 1
                # 슬로프 건설 완료 체크
                if slope_remain==0:
                    slope_remain = l
            # 슬로프 건설 진행중이 아닐 때
            else:
                margin += 1
        # 오르막길
        elif p_height<height:
            if margin>=l:
                margin = 1
            else:
                return False
        # 내리막길
        else:
            # 슬로프 건설 진행중
            if slope_remain!=l:
                return False
            # 슬로프 건설 진행중이 아닐 때
            else:
                slope_remain -= 1
                # 슬로프 건설 완료 체크
                if slope_remain==0:
                    slope_remain = l
                margin = 0
    return slope_remain==l

N, L = map(int, stdin.readline().split())
MAP = [[*map(int, i.split())] for i in stdin]
answer = 0
for row in range(N):
    if check_line(MAP[row], L):
        answer += 1
for col in range(N):
    if check_line([MAP[i][col] for i in range(N)], L):
        answer += 1
print(answer)
    


"""
코드트리 마법의 숲 탐색

1. 주차장 현재 상황과 각 차별 누적 사용시간을 dict형태로 저장
2. 이때 시간은 분정보로 변환해서 저장하면 다루기 쉬움
3. 이후 누적 사용시간을통해 적절하게 요금 계산
"""
from math import ceil

def solution(fees, records):
    park = {}
    use_times = {}
    for record in records:
        time, id, option = record.split()
        time = int(time[:2])*60+int(time[3:])
        if option[0]=="I":
            park[id] = time
        else:
            duration = time - park[id]
            del park[id]
            if id in use_times:
                use_times[id] += duration
            else:
                use_times[id] = duration
    for id, time in park.items():
        duration = 23*60+59-time
        if id in use_times:
            use_times[id] += duration
        else:
            use_times[id] = duration
    answer = []
    for id in sorted(use_times):
        use_time = use_times[id]
        base_time, base_fee, unit_time, unit_fee = fees
        if use_time<=base_time:
            answer.append(base_fee)
        else:
            use_time -= base_time
            answer.append(base_fee+ceil(use_time/unit_time)*unit_fee)
    return answer
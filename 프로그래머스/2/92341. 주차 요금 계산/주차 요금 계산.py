import math

def toMinute(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)


def solution(fees, records):
    d = {}
    answer = {}
    for r in records:
        answer[r[6:10]] = 0
    for record in records:
        time, car, state = record.split()
        if state == "IN":
            d[car] = time
        elif state == "OUT":
            answer[car] += toMinute(time) - toMinute(d[car])
            del d[car]

    if len(d) != 0: # 만약 출차기록 없는 차량 있다면... 23:59에 나간걸로 ㄱ
        for car, inTime in d.items():
            answer[car] += toMinute("23:59") - toMinute(d[car])

    for car, total in answer.items():
        if total <= fees[0]:
            answer[car] = fees[1]
        else:
            answer[car] = fees[1] + math.ceil((total - fees[0])/fees[2]) * fees[3]
    
    answer = [answer[k] for k in sorted(answer)]
    
    return answer
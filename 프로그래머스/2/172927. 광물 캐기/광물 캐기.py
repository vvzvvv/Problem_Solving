def solution(picks, minerals):
    answer = 0
    if len(minerals) > sum(picks) * 5:
        minerals = minerals[:sum(picks) * 5]
        
    minerals = [minerals[i:i+5] for i in range(0, len(minerals), 5)]
    d = {"diamond": 25, "iron": 5, "stone": 1}
    
    for i in range(len(minerals)):
        fatigue = 0
        for j in range(len(minerals[i])):
            fatigue += d[minerals[i][j]]
        minerals[i].append(fatigue)
    minerals.sort(key=lambda x: -x[-1])
    for i in minerals:
        i.remove(i[-1])
    #print(minerals)
    for mineral in minerals:
        if picks[0]: # 다이아곡괭 있다면
            answer += len(mineral)
            picks[0] -= 1 # 5개 캐고 곡괭이 소진
        elif picks[1]: # 철곡괭
            for m in mineral:
                if m == "diamond": answer += 5
                else: answer += 1
            picks[1] -= 1
        elif picks[2]: # 돌곡괭
            for m in mineral:
                answer += d[m]
            picks[2] -= 1
    return answer
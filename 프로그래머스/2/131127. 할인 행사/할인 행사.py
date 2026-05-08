from collections import Counter

def solution(want, number, discount):
    answer = 0
    d = {}
    for i in range(len(want)):
        d[want[i]] = number[i]
    
    day10 = Counter(discount[:10])
    if day10 == d: answer += 1
    
    for i in range(10, len(discount)):
        if day10[discount[i-10]] == 1:
            del day10[discount[i-10]]
        else:
            day10[discount[i-10]] -= 1
                
        if discount[i] in day10:
            day10[discount[i]] += 1
        else:
            day10[discount[i]] = 1
        
        if day10 == d: answer += 1
    return answer
from collections import Counter
def solution(weights):
    answer = 0
    c = Counter(weights)
    
    for weight in c:
        cnt = c[weight]
        if cnt > 1:
            answer += cnt * (cnt - 1) // 2
        
        for ratio in [3/2, 2, 4/3]:
            mate = weight * ratio
            if mate in c:
                answer += c[weight] * c[mate]
                
    return answer
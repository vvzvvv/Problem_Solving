from collections import defaultdict

def solution(k, tangerine):
    d = defaultdict(int)

    for size in tangerine:
        d[size] += 1

    d = sorted(d.items(), key=lambda x: x[1])
    d.reverse()
    
    cnt = 0
    result = 0
    for size, num in d:
        cnt += num
        result += 1
        if cnt >= k:
            return result
    
    return result
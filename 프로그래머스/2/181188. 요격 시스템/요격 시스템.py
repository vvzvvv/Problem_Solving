def solution(targets):
    result = 0
    targets.sort(key=lambda x: x[1])
    prev_end = 0

    for t in targets:
        if t[0] >= prev_end:
            result += 1
            prev_end = t[1]
        
    return result
def solution(n, lost, reserve):
    lost, reserve = list(set(lost) - set(reserve)), list(set(reserve) - set(lost))
    
    for re in reserve:
        for r in re - 1, re + 1: 
            if r in lost:
                lost.remove(r)
                break
                
    return n - len(lost)
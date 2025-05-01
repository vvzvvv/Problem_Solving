def solution(n, lost, reserve):
    for r in reserve[:]:
        if r in lost:
            lost.remove(r)
            reserve.remove(r)
    reserve.sort()
    arr = [-1, 1]
    for i in reserve[:]:
        for num in arr:
            if i + num in lost:
                lost.remove(i+num)
                break
    
    answer = n - len(lost)
    return answer
    
    

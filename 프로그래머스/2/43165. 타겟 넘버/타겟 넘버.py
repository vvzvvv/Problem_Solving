from itertools import product
def solution(numbers, target):
    answer = 0
    data = []
    for num in numbers:
        data.append((num, -num))
    
    s = set(product(*data))
    for t in s:
        if sum(t) == target:
            answer += 1
            
    return answer
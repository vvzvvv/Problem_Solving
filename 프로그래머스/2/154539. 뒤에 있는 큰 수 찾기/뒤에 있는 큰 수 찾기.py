def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = []
    idx = 0
    
    while idx < n:
        while stack and numbers[stack[-1]] < numbers[idx]:
            answer[stack[-1]] = numbers[idx]
            stack.pop()
        
        stack.append(idx)
        idx += 1
            
    return answer
    
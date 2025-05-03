def solution(numbers):
    answer = [-1]

    stack = [numbers[-1]]
    
    for i in range(2, len(numbers)+1):
        num = stack.pop()

        while numbers[-i] >= num:
            if not stack:
                num = -1
                break
            num = stack.pop()
        
        
        answer.append(num)
        stack.append(num)
        stack.append(numbers[-i])
        
    answer.reverse()
    return answer

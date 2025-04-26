def solution(ingredient):
    result = 0
    stack = []
    
    for i in ingredient:
        stack.append(i)
        if stack[-1:-5:-1] == [1,3,2,1]:
            for _ in range(4):
                stack.pop()
            result += 1
    
    return result
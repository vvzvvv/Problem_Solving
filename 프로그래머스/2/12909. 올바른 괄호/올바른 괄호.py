def solution(s):
    answer = True
    stack = []
    for item in s:
        if item == '(':
            stack.append(item)
        elif item == ')':
            if len(stack) == 0: return False
            
            if stack[-1:] != item:
                stack.pop()
            else:
                stack.append(item)

    return len(stack) == 0
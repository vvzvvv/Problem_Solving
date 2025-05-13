n = int(input())
result = 0
for _ in range(n):
    stack = []    
    word = input()
    
    for w in word:
        if not stack:
            stack.append(w)
        else:
            if stack[-1] == w:
                stack.pop()
            else:
                stack.append(w)
    
    if len(stack) == 0:
        result += 1
        
print(result)
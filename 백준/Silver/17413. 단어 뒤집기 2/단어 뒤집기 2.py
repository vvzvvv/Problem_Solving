s = input()
answer = []
stack = []
flag_open = False
for ch in s:
    if ch == ' ':
        while stack:
            answer.append(stack.pop())
        answer.append(ch)
        
    elif ch == '<':
        while stack:
            answer.append(stack.pop())
        answer.append(ch)
        flag_open = True
        
    elif ch == '>':
        answer.append(ch)
        flag_open = False
        
    elif flag_open:
        answer.append(ch)
        
    else:
        stack.append(ch)
        
while stack:
    answer.append(stack.pop())
    
print(''.join(answer))
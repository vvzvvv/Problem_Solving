from collections import deque

t = int(input())
for _ in range(t):
    prompts = input() # 수행할 함수
    n = int(input())
    inputs = input().replace('[', '').replace(']', '')
    
    arr = []
    for num in inputs.split(','):
        if num.isdigit():
            arr.append(int(num))
    
    arr = deque(arr)
    
    reverse = False
    error = False
    
    for p in prompts:
        if p == 'R':
            reverse = not reverse
        
        else: # p == 'D'
            if not arr:
                error = True
                break
            
            else:
                if reverse:
                    arr.pop()
                else:
                    arr.popleft()
    
    if error: print('error')
    else:
        n = len(arr)
        if n == 0:
            print('[]')
            continue
        
        result = '['
        
        if reverse:
            for i in range(n-1, -1, -1):
                result += str(arr[i])
                result += ','
        else:
            for i in range(n):
                result += str(arr[i])
                result += ','
        result = result[:-1] + ']'
        
        print(result)    
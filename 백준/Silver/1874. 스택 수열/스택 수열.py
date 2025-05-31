k = int(input())
arr = [int(input()) for _ in range(k)]
result = []
stack = []
n, idx = 1, 0

while idx < k:
    while arr[idx] >= n:
        stack.append(n)
        result.append('+')
        n += 1
        
    if not stack or stack[-1] > arr[idx]:
        print('NO')
        exit()
    
    while stack[-1] == arr[idx]:
        result.append('-')
        stack.pop()
        idx += 1
        if idx >= k or not stack:
            break

for r in result:
    print(r)
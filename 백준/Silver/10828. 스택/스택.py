import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
stack = []

for _ in range(n):
    s = input().split()
    command = s[0]
    
    if command == 'push':
        stack.append(s[1])
    elif command == 'pop':
        if len(stack) == 0: print(-1)
        else: print(stack.pop())
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if len(stack) == 0: print(1)
        else: print(0)
    elif command == 'top':
        if len(stack) == 0: print(-1)
        else: print(stack[-1])
    
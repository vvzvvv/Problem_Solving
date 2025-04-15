import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
queue = []

for _ in range(n):
    s = input().split()
    command = s[0]
    
    if command == 'push':
        queue.append(s[1])
    elif command == 'pop':
        if len(queue) == 0: print(-1)
        else: print(queue.pop(0))
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if len(queue) == 0: print(1)
        else: print(0)
    elif command == 'front':
        if len(queue) == 0: print(-1)
        else: print(queue[0])
    elif command == 'back':
        if len(queue) == 0: print(-1)
        else: print(queue[-1])

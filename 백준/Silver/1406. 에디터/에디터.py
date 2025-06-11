import sys
input = lambda: sys.stdin.readline().rstrip()

stack = list(input())
n = int(input())

temp = []

for _ in range(n):
    command = input()
    if command == 'L':
        if len(stack) != 0:
            temp.append(stack.pop())
    elif command == 'D':
        if len(temp) != 0:
            stack.append(temp.pop())
    elif command == 'B':
        if len(stack) != 0:
            stack.pop()
    elif command[0] == 'P':
        stack.append(command[2])
        
if len(temp) > 0:
    temp.reverse()
    stack += temp
print(''.join(stack))
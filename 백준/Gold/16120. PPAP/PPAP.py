import sys
input = lambda: sys.stdin.readline().rstrip()

word = list(input())
stack = []
ppap = ['P', 'P', 'A', 'P']

for i in range(len(word)):
    stack.append(word[i])
    if len(stack) >= 4:
        if stack[-4:] == ['P', 'P', 'A', 'P']:
            stack.pop()
            stack.pop()
            stack.pop()
            
if stack == ['P']:
    print('PPAP')
else:
    print('NP')
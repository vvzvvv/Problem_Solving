a, b, c = map(int, input().split())

if c <= b:
    print(-1)
else: 
    num = a / (c - b)
    n = int(num) + 1
    print(n)

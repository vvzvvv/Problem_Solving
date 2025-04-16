n, m = map(int, input().split())
data = list(map(int, input().split()))

def one(a, i, x):
    data[i-1] = x
    
def two(a, l, r):
    for i in range(l-1, r):
        #data[i] = not data[i]
        data[i] = abs(data[i] - 1)

def three(a, l, r):
    for i in range(l-1, r):
        data[i] = 0
        
def four(a, l, r):
    for i in range(l-1, r):
        data[i] = 1



for i in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        one(a, b, c)
    elif a == 2:
        two(a, b, c)
    elif a == 3:
        three(a, b, c)
    elif a == 4:
        four(a, b, c)
        
for i in data:
    print(i, end=' ')
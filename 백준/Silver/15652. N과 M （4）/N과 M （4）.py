n, m = map(int, input().split())

arr = []
def func(depth, start):
    if depth == m:
        print(*arr)
        return
    
    for i in range(start, n+1):
        arr.append(i)
        func(depth + 1, i)
        arr.pop()

func(0, 1)
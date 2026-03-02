n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
path = [0] * m

def func(depth):
    if depth == m:
        print(*path)
        return
    
    for i in range(n):
        path[depth] = arr[i]
        func(depth + 1)
        
func(0)
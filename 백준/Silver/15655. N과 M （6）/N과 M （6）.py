n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
path = [0] * m

def func(start, depth):
    if depth == m:
        print(*path)
        return
    
    for i in range(start, n):
        path[depth] = arr[i]
        func(i + 1, depth + 1)
        
func(0, 0)
n, m = map(int, input().split())
arr = [num for num in range(1, n + 1)]
path = [0 for _ in range(m)]

def func(cnt):
    if cnt == m:
        print(*path)
        return
    
    for i in range(n):
        path[cnt] = arr[i]
        func(cnt + 1)

func(0)
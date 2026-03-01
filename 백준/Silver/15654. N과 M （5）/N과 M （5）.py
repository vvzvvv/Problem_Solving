n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [0] * n
path = [0] * m

def func(depth):
    if depth == m:
        print(*path)
        return
    
    for i in range(n):
        if not visited[i]:
            path[depth] = arr[i]
            visited[i] = 1
            func(depth + 1)
            visited[i] = 0

func(0)
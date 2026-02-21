# 재풀이 (260220)
n, m = map(int, input().split())
visited = [False] * (n + 1) 
arr = []

def func(n, m):
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(1, n+1):
        if not visited[i]:
            arr.append(i)
            visited[i] = True
            func(n, m)
            arr.pop()
            visited[i] = False

func(n, m)

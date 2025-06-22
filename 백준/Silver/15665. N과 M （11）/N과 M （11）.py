n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [0] * n
result = []

def func(depth):
    if depth == m:
        print(*result)
        return
    for i in range(n):
        if i > 0 and arr[i] == arr[i-1] and not visited[i-1]: continue

        result.append(arr[i])
        visited[i] = 1
        func(depth + 1)
        result.pop()
        visited[i] = 0
func(0)
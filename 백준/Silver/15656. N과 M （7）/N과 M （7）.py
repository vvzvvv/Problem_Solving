n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = []

def func(depth):
    if depth == m:
        print(*result)
        return
    for i in range(n):
        result.append(arr[i])
        func(depth + 1)
        result.pop()
func(0)
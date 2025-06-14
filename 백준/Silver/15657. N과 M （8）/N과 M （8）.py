n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = []

def func(depth, start):
    if depth == m:
        print(*result)
        return
    for i in range(start, n):
        result.append(arr[i])
        func(depth + 1, i)
        result.pop()
        
func(0, 0)
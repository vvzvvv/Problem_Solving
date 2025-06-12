n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = []


def func(depth, start_idx):
    if depth == m:
        print(*result)
        return
    for i in range(start_idx, n):
        result.append(arr[i])
        func(depth + 1, i + 1)
        result.pop()
func(0, 0)

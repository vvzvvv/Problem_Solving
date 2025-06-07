n, m = map(int, input().split())
arr = []
def func(k):
    if k == m:
        print(*arr)
        return
    for i in range(1, n+1):
        arr.append(i)
        func(k+1)
        arr.pop()
func(0)
n, m = map(int, input().split())
visited = [0] * (n + 1)
arr = []

def func(start, arr):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(start, n + 1):
        #new_arr = arr + [i]
        func(i + 1, arr + [i])
    
func(1, arr)
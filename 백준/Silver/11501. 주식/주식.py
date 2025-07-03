t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = 0
    maxval = arr[-1]
    for i in range(n-1, -1, -1):
        if arr[i] < maxval:
            result += maxval - arr[i]
        else:
            maxval = arr[i]
    print(result)
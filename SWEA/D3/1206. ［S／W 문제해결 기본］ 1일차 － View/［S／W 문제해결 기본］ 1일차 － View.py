for case in range(10):
    res = 0
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(2, n-2):
        lst = arr[i-2:i] + arr[i+1:i+3]
        if max(lst) < arr[i]:
            res += arr[i] - max(lst)
    print(f'#{case+1} {res}')
n, k = map(int, input().split())
arr = [x for x in range(2, n+1)]
result = [0] * (k + 1)
cnt = 0
while len(arr) != 0 and result[-1] == 0:
    p = arr[0]
    arr.remove(p)
    cnt += 1
    result[cnt] = p
    
    i = 2
    while len(arr) != 0 and p * i <= arr[-1]:
        try:
            arr.remove(p*i)
            cnt += 1
            result[cnt] = p*i
        except:
            pass
        i += 1
        
print(result[-1])

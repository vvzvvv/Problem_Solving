n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
p1, p2 = 0, 0
total = 0

while 1:
    if total >= m:
        if total == m:
            cnt += 1
        total -= arr[p1]
        p1 += 1
    
    elif p2 == n:
        break
    
    else:
        total += arr[p2]
        p2 += 1

print(cnt)
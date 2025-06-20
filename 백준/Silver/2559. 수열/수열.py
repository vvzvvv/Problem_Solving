n, k = map(int, input().split())
arr = list(map(int, input().split()))

total = sum(arr[:k])
p1, p2 = 0, k
mxval = -100 * k

while p2 < n:
    if total > mxval:
        mxval = total
    
    total += arr[p2] - arr[p1]
    p1 += 1
    p2 += 1

if total > mxval:
    mxval = total    

print(mxval)
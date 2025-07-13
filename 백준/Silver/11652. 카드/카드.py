n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
arr.append(2**62+1)

cnt = 1
mxval = arr[0]
mxcnt = 0

for i in range(1, n+1):
    if arr[i-1] == arr[i]:
        cnt += 1
    else:
        if cnt > mxcnt:
            mxcnt = cnt
            mxval = arr[i-1]
        cnt = 1

print(mxval)
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
s = 0

for idx in range(n):
    maxval = -1
    for i in range(n):
        if b[i] > maxval:
            maxval = b[i]
            maxidx = i
    s += a[idx] * b[maxidx]
    b[maxidx] = -1

print(s)
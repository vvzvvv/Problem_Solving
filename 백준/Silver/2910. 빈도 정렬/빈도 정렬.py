n, c = map(int, input().split())
d = {}
arr = list(map(int, input().split()))
for i in range(n):
    if arr[i] not in d:
        d[arr[i]] = 1
    else:
        d[arr[i]] += 1

for k, v in sorted(d.items(), key=lambda x : -x[1]):
    for _ in range(v):
        print(k, end=' ')

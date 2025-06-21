n, target = map(int, input().split())
arr = list(map(int, input().split()))
count = dict()
count[0] = 1
cnt = 0
prefix = 0

for a in arr:
    prefix += a
    cnt += count.get(prefix - target, 0)
    count[prefix] = count.get(prefix, 0) + 1

print(cnt)

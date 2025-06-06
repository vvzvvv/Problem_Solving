n = int(input())
d = {}
for _ in range(n):
    name, file = input().split('.')
    if file not in d:
        d[file] = 1
    else:
        d[file] += 1

for k, v in sorted(d.items()):
    print(k, v)
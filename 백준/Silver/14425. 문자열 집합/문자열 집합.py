n, m = map(int, input().split())
d = {}
for _ in range(n):
    d[input()] = 1

cnt = 0
for _ in range(m):
    word = input()
    if word in d:
        cnt += 1
print(cnt)
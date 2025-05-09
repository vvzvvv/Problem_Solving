n, m, now = map(int, input().split())

hate2like = {}
for _ in range(n):
     like, hate = map(int, input().split())
     if hate in hate2like: continue
     hate2like[hate] = like

visited = set()
cnt = 0
while now in hate2like:
    if now in visited:
        print(-1)
        break
    visited.add(now)
    now = hate2like[now]
    cnt += 1

else:
    print(cnt)

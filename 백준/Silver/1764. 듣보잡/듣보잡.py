n, m = map(int, input().split())
listen = set()
see = set()

for _ in range(n):
    listen.add(input())
for _ in range(m):
    see.add(input())

listen_see =listen.intersection(see)
print(len(listen_see))
for name in sorted(listen_see):
    print(name)

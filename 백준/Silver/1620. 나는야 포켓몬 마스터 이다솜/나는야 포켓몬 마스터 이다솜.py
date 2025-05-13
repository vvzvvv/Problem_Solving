n, m = map(int, input().split())
d = {}
for i in range(n):
    pokemon = input()
    num = str(i+1)
    d[pokemon] = num
    d[num] = pokemon

for _ in range(m):
    word = input()
    print(d[word])
n1, n2 = map(int, input().split())
small, big = min(n1, n2), max(n1, n2)

lst = []
for i in range(1, round(small ** 0.5) + 1):
    if small % i == 0:
        lst.append(i)
        lst.append(small//i)

lst.sort(reverse=True)
for i in lst:
    if big % i == 0:
        print(i)
        break


for i in range(1, big+1):
    if (small * i) % big == 0:
        print(small * i)
        break
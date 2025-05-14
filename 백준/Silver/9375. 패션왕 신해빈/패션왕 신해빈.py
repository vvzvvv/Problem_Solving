case = int(input())

for _ in range(case):
    n = int(input())
    d = {}
    for _ in range(n):
        name, kind = input().split()
        if kind not in d:
            d[kind] = 1
        else:
            d[kind] += 1
    
    res = 1
    for v in d.values():
        res *= v + 1
    print(res-1)
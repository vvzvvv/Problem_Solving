n = int(input())
d = [-1] * 100001
d[2] = 1
d[5] = 1

for i in range(4, n+1):
    if d[i-5] == -1 and d[i-2] == -1:
        pass
    elif d[i-5] == -1:
        d[i] = d[i-2] + 1
    else:    
        d[i] = min(d[i-2] + 1, d[i-5] + 1)

print(d[n])
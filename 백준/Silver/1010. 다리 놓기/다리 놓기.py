t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    
    res1 = 1
    a = n
    while a > 0:
        res1 *= a
        a -= 1
   
    res2 = 1
    b = m
    while b >= m - n + 1:
        res2 *= b
        b -= 1

    print(res2//res1)
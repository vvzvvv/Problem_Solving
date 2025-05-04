from math import isqrt

n = int(input())
lst = list(map(int, input().split()))

m = min(lst) # 입력 중 최솟값
cd = set()
for n in range(1, isqrt(m) + 1):
    if m % n == 0:
        cd.add(n)
        cd.add(m//n)
    
for n in sorted(cd):
    if all(num % n == 0 for num in lst):
        print(n)
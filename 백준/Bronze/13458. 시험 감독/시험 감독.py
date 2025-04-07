import math

n = int(input())
arr = list(map(int, input().split()))
a, b = map(int, input().split())

result = 0
for ai in arr:
    num = 1
    ai -= a
    if ai <= 0:
        result += num
        continue
    num += math.ceil(ai / b)
    result += num
    
print(result)
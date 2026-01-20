import math

num = input()
arr = [0 for _ in range(10)]

for n in num:
    arr[int(n)] += 1

half = math.ceil((arr[6] + arr[9]) / 2)
arr[6], arr[9] = half, half

print(max(arr))


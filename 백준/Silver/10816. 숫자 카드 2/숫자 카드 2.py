from collections import defaultdict

n = int(input())
arr_n = list(map(int, input().split()))

numbers = defaultdict(int)
for i in range(n):
    numbers[arr_n[i]] += 1

m = int(input())
arr_m = list(map(int, input().split()))
result = []
for i in range(m):
    if arr_m[i] in numbers:
        result.append(numbers[arr_m[i]])
    else:
        result.append(0)
print(*result)
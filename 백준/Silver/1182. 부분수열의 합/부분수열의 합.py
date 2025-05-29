from itertools import product

N, S = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
data = []
for num in arr:
    data.append((num, 0))

s = list(product(*data))

for t in s:
    if sum(t) == S:
        result += 1

if S == 0: result -= 1

print(result)
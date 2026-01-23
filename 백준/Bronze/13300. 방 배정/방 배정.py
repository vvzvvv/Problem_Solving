import math

n, k = map(int, input().split())

girl = [0 for _ in range(7)]
boy = [0 for _ in range(7)]

for _ in range(n):
    s, y = map(int, input().split())
    if s == 0:
        girl[y] += 1
    else:
        boy[y] += 1

result = 0
for i in range(1, 7):
    result += math.ceil(girl[i] /k)
    result += math.ceil(boy[i] /k)

print(result)
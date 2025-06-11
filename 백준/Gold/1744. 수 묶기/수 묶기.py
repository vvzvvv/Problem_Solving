n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
result = 0
plus, minus = [], []
zero, one = 0, 0

for i in range(n):
    if arr[i] == 1:
        one += 1
    elif arr[i] == 0:
        zero += 1
    elif arr[i] > 0:
        plus.append(arr[i])
    elif arr[i] < 0:
        minus.append(arr[i])

plus.reverse()
for i in range(0, len(plus), 2):
    if i == len(plus) - 1:
        result += plus[i]
    else:
        result += plus[i] * plus[i+1]

for i in range(0, len(minus), 2):
    if i == len(minus) - 1:
        if not zero:
            result += minus[i]
    else:
        result += minus[i] * minus[i+1]

result += one
print(result)
        
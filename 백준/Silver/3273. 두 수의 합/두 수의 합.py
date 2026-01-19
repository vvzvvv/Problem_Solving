n = int(input())
lst = list(map(int, input().split()))
arr = [0 for _ in range(1000001)]
for num in lst:
    arr[num] = 1

x = int(input())

result = 0
for i in range(1000001):
    if arr[i] and (x - i <= 1000000) and arr[x - i] and (x - i != i):
        arr[i] = 0
        result += 1

print(result)
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

result = arr[0]
num = 1
for i in range(1, n):
    num += 1
    if arr[i] * num > result:
        result = arr[i] * num

print(result)
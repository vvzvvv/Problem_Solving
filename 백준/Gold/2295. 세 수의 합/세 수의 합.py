n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

twoSum = set()
for i in range(n):
    for j in range(n):
        twoSum.add(arr[i] + arr[j])

for i in range(n-1, 0, -1):
    for j in range(i):
        if arr[i] - arr[j] in twoSum:
            print(arr[i])
            exit()
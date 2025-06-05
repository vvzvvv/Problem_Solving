n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)

total = 0
for i in range(n):
    if (i + 1) % 3 == 0:
        continue
    total += arr[i]

print(total)
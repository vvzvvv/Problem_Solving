n = int(input())
target = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
cnt = 0

i, j = 0, n-1
while i < j:
    total = numbers[i] + numbers[j]
    if total < target:
        i += 1
    elif total > target:
        j -= 1
    else:
        cnt += 1
        i += 1
print(cnt)
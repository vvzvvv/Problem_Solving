arr = [0 for _ in range(26)]

for word in input():
    arr[ord(word) - 97] += 1

print(*arr)
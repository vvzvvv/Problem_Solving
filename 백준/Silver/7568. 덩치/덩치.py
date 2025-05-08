n = int(input())

arr = []
result = []

for _ in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])

for i in range(n):
    number = 1
    
    for j in range(n):
        if i == j: continue
        
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            number += 1
    result.append(number)

for a in result:
    print(a, end=' ')
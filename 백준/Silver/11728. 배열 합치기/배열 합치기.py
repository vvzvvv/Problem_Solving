n, m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
result = []
p1, p2 = 0, 0
while p1 < n and p2 < m:
    if arr1[p1] > arr2[p2]:
        result.append(arr2[p2])
        p2 += 1
    elif arr1[p1] < arr2[p2]:
        result.append(arr1[p1])
        p1 += 1
    else: # 같을 때
        result.append(arr1[p1])
        result.append(arr2[p2])
        p1 += 1
        p2 += 1
        
if p1 == n:
    result += arr2[p2:]
else:
    result += arr1[p1:]

print(*result)
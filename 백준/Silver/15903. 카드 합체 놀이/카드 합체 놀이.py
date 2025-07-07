n, m = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(m):
    arr.sort(reverse=True)
    sumval = arr.pop() + arr.pop()
    arr.append(sumval)
    arr.append(sumval)
    
print(sum(arr))
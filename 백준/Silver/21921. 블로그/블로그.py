n, x = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 1

total = 0
for i in range(0, x):
    total += arr[i]
max_v = total
start = 0
end = x-1

while end < n-1:
    total -= arr[start]
    total += arr[end+1]
    start += 1
    end += 1
    
    if total > max_v:
        max_v = total
        cnt = 1
    elif total == max_v:
        cnt += 1

if max_v == 0:
    print("SAD")
else:
    print(max_v)
    print(cnt)
        
    
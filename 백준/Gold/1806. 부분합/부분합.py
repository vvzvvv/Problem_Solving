n, s = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
cur_sum = 0
cur_len = 0
min_len = 100001
for right in range(n):
    cur_sum += arr[right]
    cur_len += 1
    
    while cur_sum >= s:
        if cur_len < min_len:
            min_len = cur_len
            
        cur_sum -= arr[left]
        cur_len -= 1
        left += 1

if min_len == 100001: print(0)
else: print(min_len)
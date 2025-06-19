n = int(input()) 
arr = [int(input()) for _ in range(n)]
arr.sort()

# max_value = -(2**62 + 1)
max_cnt = 0
cnt = 0
value = -(2**62 + 1)

for i in range(n):
    if arr[i] != value:
        if cnt > max_cnt:
            max_cnt = cnt
            max_value = value
        value = arr[i]
        cnt = 1
    else:
        cnt += 1
if cnt > max_cnt:
    max_value = arr[-1]

print(max_value)
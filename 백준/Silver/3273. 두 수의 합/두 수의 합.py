n = int(input())
lst = list(map(int, input().split()))
lst.sort()
left = 0
right = n-1
x = int(input())

result = 0
while 1:
    if left >= right: break
    
    sum_num = lst[left] + lst[right]
    
    if sum_num == x:
        result += 1
        left += 1
        right -= 1
    elif sum_num > x:
        right -= 1
    else:
        left += 1

print(result)
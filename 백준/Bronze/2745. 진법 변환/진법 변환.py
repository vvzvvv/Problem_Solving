n, b = input().split()
b = int(b)
result, m = 0, len(n) - 1

for num in n:
    if 65 <= ord(num) <= 90:
        num = ord(num) - 55
    else:
        num = int(num)

    result += (b ** m) * num
    m -= 1
print(result)
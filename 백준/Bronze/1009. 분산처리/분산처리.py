n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    num = b % 4
    if num == 0: num = 4
    result = a ** num % 10
    if result == 0: print(10)
    else: print(result)
result = 0
diff = 100

for _ in range(10):
    num = int(input())
    result += num
    di = abs(100 - result)
    
    if result >= 100:
        if di <= diff: break
        else:
            result -= num
            break
    else:
        diff = di

print(result)
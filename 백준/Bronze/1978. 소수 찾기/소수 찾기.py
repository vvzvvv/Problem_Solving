n = int(input())
arr = list(map(int, input().split()))

result = 0

for i in arr:
    if i == 1: continue
    
    num = 0 # 약수 개수
    for j in range(1, i+1):
        if i % j == 0: num += 1
    
    if num == 2: result += 1    

print(result)
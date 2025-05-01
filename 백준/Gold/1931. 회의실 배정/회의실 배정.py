n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])

arr.sort(key=lambda x:(x[1], x[0]))
#print(arr)
cur_end = 0
result = 0

for s, e in arr:
    if s >= cur_end :
        cur_end = e
        result += 1
        
print(result)

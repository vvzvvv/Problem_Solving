from collections import deque

n, m = map(int, input().split())
arr = list(map(int, input().split()))

deq = deque([num for num in range(1, n + 1)])
result = 0

for i in range(m):
    idx = deq.index(arr[i])
    leng = len(deq)
    
    if idx <= leng - idx:
        for _ in range(idx):
            num = deq.popleft()
            deq.append(num)
        result += idx
    else:
        for _ in range(leng - idx):
            num = deq.pop()
            deq.appendleft(num)
        result += leng - idx
            
    deq.popleft()

print(result)
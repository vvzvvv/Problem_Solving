import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

result = [[0] * m for _ in range(n)]

layers = min(n, m) // 2

for i in range(layers):
    q = deque()
    
    for j in range(i, m - i - 1):
        q.append(arr[i][j])

    for j in range(i, n - i - 1):
        q.append(arr[j][m - i - 1])
    
    for j in range(m - i - 1, i, -1):
        q.append(arr[n - i - 1][j])
    
    for j in range(n - i - 1, i, -1):
        q.append(arr[j][i])
        
    q.rotate(-r)
    
    for j in range(i, m - i - 1):
        result[i][j] = q.popleft()
    
    for j in range(i, n - i - 1):
        result[j][m - i - 1] = q.popleft()

    for j in range(m - i - 1, i, -1):
        result[n - i - 1][j] = q.popleft()
        
    for j in range(n - i - 1, i, -1):
        result[j][i] = q.popleft()

for row in result:
    print(*(row))
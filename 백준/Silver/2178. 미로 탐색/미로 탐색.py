from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    row = []
    for i in input():
        row.append(int(i))
    graph.append(row)
        
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

que = deque([(0, 0)])

while que:
    x, y = que.popleft()
    
    if x == n-1 and y == m-1:
        print(graph[x][y])
        break
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            que.append((nx, ny))
 
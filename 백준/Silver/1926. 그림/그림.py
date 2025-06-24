from collections import deque 

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    size = 0
    while queue:
        x, y = queue.popleft()
        size += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if board[nx][ny] == 0 or visited[nx][ny]: continue
            
            visited[nx][ny] = 1
            queue.append((nx, ny))
    return size

cnt = 0
max_size = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and visited[i][j] == 0:
            size = bfs(i, j)
            cnt += 1
            if size > max_size:
                max_size = size

print(cnt)
print(max_size)
            
from collections import deque

n, m, k = map(int, input().split())
board = [[0] * m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    que = deque([(x, y)])
    board[x][y] = 0
    food = 1
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == 1:
                que.append((nx, ny))
                board[nx][ny] = 0
                food += 1
    return food
            
result = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            food = bfs(i, j)
            if food > result:
                result = food

print(result)

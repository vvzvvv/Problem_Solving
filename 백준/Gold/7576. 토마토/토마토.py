from collections import deque

m, n = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

que = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            que.append((i, j))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

while que:
    x, y = que.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
        if board[nx][ny] == 0:
            board[nx][ny] = board[x][y] + 1
            que.append((nx, ny))

result = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            print(-1)
            exit()
        if board[i][j] > result:
            result = board[i][j]

print(result - 1)

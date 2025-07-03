from collections import deque
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 시작 위치 찾기 & 0 위치 visited에 대입
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            sx, sy = i, j
        elif board[i][j] == 0:
            visited[i][j] = 0

que = deque()
que.append((sx, sy))
visited[sx][sy] = 0
while que:
    x, y = que.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
        if visited[nx][ny] != -1: continue
        visited[nx][ny] = visited[x][y] + 1
        que.append((nx, ny))

for v in visited:
    print(*v)
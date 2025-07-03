from collections import deque

m, n, h = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[-1] * m for _ in range(n)] for _ in range(h)]

dz = [0, 0, 0, 0, -1, 1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]

que = deque()
for z in range(h):
    for x in range(n):
        for y in range(m):
            # 토마토 있는 곳 큐에 삽입, 거리 0 처리
            if board[z][x][y] == 1:
                que.append((z, x, y))
                visited[z][x][y] = 0
            # 토마토 없는 곳은 방문 처리
            elif board[z][x][y] == -1:
                visited[z][x][y] = 0
                

while que:
    z, x, y = que.popleft()
    for d in range(6):
        nz = z + dz[d]
        nx = x + dx[d]
        ny = y + dy[d]
        if not(0 <= nz < h and 0 <= nx < n and 0 <= ny < m):
            continue
        if visited[nz][nx][ny] != -1 or board[nz][nx][ny] == -1: continue
        
        visited[nz][nx][ny] = visited[z][x][y] + 1
        que.append((nz, nx, ny))

maxval = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if visited[z][x][y] == -1:
                print(-1)
                exit()
            if visited[z][x][y] > maxval:
                maxval = visited[z][x][y]

print(maxval)
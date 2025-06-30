from collections import deque

m, n, k = map(int, input().split())
board = [[0] * m for _ in range(n)]

for _ in range(k):
    sx, sy, ex, ey = map(int, input().split())
    for x in range(sx, ex):
        for y in range(sy, ey):
            board[x][y] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            cnt = 1
            que = deque()
            que.append((i, j))
            board[i][j] = 1
            while que:
                x, y = que.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    
                    if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
                    if board[nx][ny] != 0: continue
                    cnt += 1
                    board[nx][ny] = 1
                    que.append((nx, ny))
            result.append(cnt)

print(len(result))
result.sort()
print(*result)
    
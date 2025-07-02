from collections import deque

n = int(input())
board = [list(input()) for _ in range(n)]
vis1 = [[0] * n for _ in range(n)]
vis2 = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 비적록색약인
que = deque()
cnt = 0
for i in range(n):
    for j in range(n):
        if not vis1[i][j]:
            cnt += 1
            que.append((i, j))
            vis1[i][j] = 1
            color = board[i][j]
            while que:
                x, y = que.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    
                    if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
                    if vis1[nx][ny] or board[nx][ny] != color: continue
                    
                    vis1[nx][ny] = 1
                    que.append((nx, ny))
print(cnt, end=' ')
    
# 비적록색약인
que = deque()
cnt = 0
for i in range(n):
    for j in range(n):
        if not vis2[i][j]:
            cnt += 1
            que.append((i, j))
            color = board[i][j]
            while que:
                x, y = que.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    
                    if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
                    if vis2[nx][ny]: continue
                    if color == 'B' and board[nx][ny] != 'B':continue
                    if color in ('R', 'G') and board[nx][ny] == 'B': continue
                    
                    vis2[nx][ny] = 1
                    que.append((nx, ny))
print(cnt)

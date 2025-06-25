from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            queue.append((i, j, 1))

while queue:
    x, y, day = queue.popleft()
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
        if board[nx][ny] == -1: continue
        if board[nx][ny] == 0:
            board[nx][ny] = day
            queue.append((nx, ny, day + 1))

max_val = 0
for i in range(n):
    if 0 in board[i]:
        print(-1)
        exit()
    for j in range(m):
        if board[i][j] > max_val:
            max_val = board[i][j]
if max_val == 1:
    print(0)
else: print(max_val)
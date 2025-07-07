from collections import deque
# 비버굴 D
# 고슴도치 위치 S
# 빈 곳 . 물 * 돌 X
# 물은 매 분 빈 칸으로 확장

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
vis1 = [[-1] * c for _ in range(r)]
vis2 = [[-1] * c for _ in range(r)]
que1 = deque() # 물
que2 = deque() # 고슴도치

for i in range(r):
    for j in range(c):
        if board[i][j] == '*':
            que1.append((i, j))
            vis1[i][j] = 0
        elif board[i][j] == 'S':
            que2.append((i, j))
            vis2[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while que1:
    x, y = que1.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= r or ny < 0 or ny >= c: continue
        if board[nx][ny] == 'X' or vis1[nx][ny] != -1: continue
        if board[nx][ny] == 'D': continue # 비버 굴 못 감
        vis1[nx][ny] = vis1[x][y] + 1
        que1.append((nx, ny))

while que2:
    x, y = que2.popleft()
    
    if board[x][y] == 'D':
        print(vis2[x][y])
        break
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= r or ny < 0 or ny >= c: continue
        if board[nx][ny] == 'X' or vis2[nx][ny] != -1: continue
        if vis1[nx][ny] == -1 or vis1[nx][ny] > vis2[x][y] + 1:
            vis2[nx][ny] = vis2[x][y] + 1
            que2.append((nx, ny))
else:
    print("KAKTUS")
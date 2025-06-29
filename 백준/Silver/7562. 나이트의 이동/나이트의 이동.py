from collections import deque

tc = int(input())

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

for _ in range(tc):
    l = int(input())
    board = [[-1] * l for _ in range(l)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    
    que = deque()
    que.append((sx, sy))
    board[sx][sy] = 0
    
    while que:
        x, y = que.popleft()
        
        if x == ex and y == ey:
            print(board[x][y])
            break
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if board[nx][ny] >= 0: continue
            
            board[nx][ny] = board[x][y] + 1
            que.append((nx, ny))
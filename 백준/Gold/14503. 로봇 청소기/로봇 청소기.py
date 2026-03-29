n, m = map(int, input().split())
x, y, d = map(int, input().split())
# d 북0, 동1, 남2, 서3 (반시계 - 북, 서, 남, 동)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

result = 0
while 1:
    # 현재 칸 청소 X ? => 청소 Go
    if board[x][y] == 0:
        board[x][y] = '-'
        result += 1
        
    dirty = False
    for i in range(1, 5):
        nd = (d - i + 4) % 4
        nx, ny = x + dx[nd], y + dy[nd]
    
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if board[nx][ny] == 0:
            x, y, d = nx, ny, nd
            dirty = True
            break
        
    # 4칸 중 청소안된 곳 X => 후진
    if not dirty:
        x -= dx[d]
        y -= dy[d]
        if x < 0 or x >= n or y < 0 or y >= m or board[x][y] == 1:
            print(result)
            exit()
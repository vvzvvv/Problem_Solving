from collections import deque

def solution(board):
    answer = 0
    row = len(board)
    col = len(board[0])
    for x in range(row):
        for y in range(col):
            if board[x][y] == "R":
                start = (x, y)
            elif board[x][y] == "G":
                goal = (x, y)
    
    dist = [[float('inf')] * col for _ in range(row)]
    dist[start[0]][start[1]] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    #def bfs(start, goal):
    queue = deque()
    queue.append(start)
    while queue:
        x, y = queue.popleft()
        if (x, y) == goal:
            return dist[x][y]

        for i in range(4):
            nx, ny = x, y
            while True:
                nx += dx[i]
                ny += dy[i]
                if nx < 0 or nx >= row or ny < 0 or ny >= col or board[nx][ny] == "D":
                    nx -= dx[i]
                    ny -= dy[i]
                    break
                    
            if dist[nx][ny] > dist[x][y] + 1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    return -1
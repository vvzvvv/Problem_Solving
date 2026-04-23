from collections import deque

def solution(board):
    n, m = len(board), len(board[0])
    visited = [[float('inf')] * m for _ in range(n)]
    que = deque()
    cnt = 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R': # 시작 위치
                for d in range(4):
                    que.append((i, j, d, cnt))
            elif board[i][j] == 'G': # 종료 위치
                ex, ey = i, j
    
    while que:
        x, y, d, cnt = que.popleft()
        while 1:
            nx, ny = x + dx[d], y + dy[d]
            if not(0 <= nx < n and 0 <= ny < m) or board[nx][ny] == 'D':
                if visited[x][y] > cnt + 1:
                    visited[x][y] = cnt + 1
                    for di in range(4):
                        que.append((x, y, di, cnt + 1))
                break
            x, y = nx, ny

    if visited[ex][ey] == float('inf'): return -1
    else: return visited[ex][ey]
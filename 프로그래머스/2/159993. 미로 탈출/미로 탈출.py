from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S': start = (i, j)
            elif maps[i][j] == 'L': lever = (i, j)
            elif maps[i][j] == 'E': end = (i, j)
    
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    def bfs(start, goal):
        que = deque([(start[0], start[1], 0)])
        visited = [[float('inf')] * m for _ in range(n)]
        
        while que:
            x, y, cnt = que.popleft()
            if (x, y) == goal:
                return cnt

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if not (0 <= nx < n and 0 <= ny < m) or maps[nx][ny] == 'X':
                    continue
                if visited[nx][ny] > cnt + 1:
                    visited[nx][ny] = cnt + 1
                    que.append((nx, ny, cnt + 1))
                    
        return False
    
    to_lever = bfs(start, lever)
    to_end = bfs(lever, end)
    if to_lever and to_end: return to_lever + to_end
    return -1
    
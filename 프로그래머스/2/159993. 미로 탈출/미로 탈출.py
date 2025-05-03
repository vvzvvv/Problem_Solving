from collections import deque

def solution(maps):
    for x, row in enumerate(maps):
        for y, item in enumerate(row):
            if maps[x][y] == "S":
                start_x, start_y = x, y
            elif maps[x][y] == "L":
                lever_x, lever_y = x, y
    
    def bfs(sx, sy, target):
        dist = [[float('inf')] * len(maps[0]) for _ in range(len(maps))]
        dist[sx][sy] = 0
        que = deque()
        que.append((sx, sy))
        
        while que:
            x, y = que.popleft()
            if maps[x][y] == target:
                return dist[x][y]
            
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 'X':
                    if dist[nx][ny] > dist[x][y] + 1:
                        dist[nx][ny] = dist[x][y] + 1
                        que.append((nx, ny))
        return -1
    
    mid_length = bfs(start_x, start_y, "L")
    if mid_length == -1: return -1
    
    length = bfs(lever_x, lever_y, "E")
    if length == -1: return -1

    return mid_length + length
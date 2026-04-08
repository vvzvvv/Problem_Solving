from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

result = 0
que = deque([])
for i in range(n):
    for j in range(m):
        if lab[i][j] == 9:
            if visited[i][j] == 0: result += 1
            visited[i][j] = 15
            for d in range(4):
                que.append((i, j, d))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while que:
    x, y, d = que.popleft()
    nx, ny = x + dx[d], y + dy[d]

    if not (0 <= nx < n and 0 <= ny < m): continue
    if visited[nx][ny] & (1 << d): continue
    
    if visited[nx][ny] == 0:
        result += 1
    
    visited[nx][ny] |= (1 << d)
    
    nd = d
    obj = lab[nx][ny]
    if obj == 1:
        if d == 2 or d == 3: continue
    elif obj == 2:
        if d == 0 or d == 1: continue
    elif obj == 3:
        nd = d ^ 3
    elif obj == 4:
        nd = d ^ 2
    elif obj == 9: continue
    
    que.append((nx, ny, nd))


print(result)

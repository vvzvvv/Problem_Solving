from collections import deque

n = int(input())
board = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
result = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not visited[i][j]:
            que = deque()
            que.append((i, j))
            visited[i][j] = 1 # 방문 처리
            cnt = 1
            
            while que:
                x, y = que.popleft()
                for d in range(4): # i (X)
                    nx = x + dx[d]
                    ny = y + dy[d]
                    
                    if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
                    if board[nx][ny] == 0 or visited[nx][ny]: continue
                    
                    visited[nx][ny] = 1
                    cnt += 1
                    que.append((nx, ny))
            result.append(cnt)

print(len(result))
result.sort()
print(*result, sep='\n')
from itertools import combinations 
from collections import deque
import copy

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

empty = [(i, j) for i in range(n) for j in range(m) if board[i][j] == 0]
virus = [(i, j) for i in range(n) for j in range(m) if board[i][j] == 2]

result = 0
for walls in combinations(empty, 3):
    bo = copy.deepcopy(board)
    for wall in walls:
        bo[wall[0]][wall[1]] = 1
    que = deque(virus[:])
    
    while que:
        x, y = que.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if bo[nx][ny] == 0:
                bo[nx][ny] = 2
                que.append((nx, ny))
    
    answer = 0
    for i in range(n):
        for j in range(m):
            if bo[i][j] == 0:
                answer += 1
                
    if answer > result:
        result = answer

print(result)

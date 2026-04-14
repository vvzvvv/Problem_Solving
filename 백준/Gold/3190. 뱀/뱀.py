from collections import deque

n = int(input())
board = [[0] * n for _ in range(n)]

# 사과(1) 배치
k = int(input())
for _ in range(k):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1

def turn(cur_d, new_d):
    if new_d == 'D':
        if cur_d == 0: return 3
        elif cur_d == 1: return 2
        elif cur_d == 2: return 0 
        else: return 1
    else:
        if cur_d == 0: return 2
        elif cur_d == 1: return 3
        elif cur_d == 2: return 1 
        else: return 0

dic = dict()
for _ in range(int(input())):
    at_time, new_d = input().split()
    dic[int(at_time)] = new_d

# 상0 하1 좌2 우3
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

snake = deque([(0, 0)])
cur_time = 0
x, y, d = 0, 0, 3

while 1:
    cur_time += 1
    nx, ny = x + dx[d], y + dy[d]
    
    if nx < 0 or nx >= n or ny < 0 or ny >= n or (nx, ny) in snake:
        break
    
    snake.appendleft((nx, ny))
    
    if board[nx][ny] == 0:
        snake.pop()
    elif board[nx][ny] == 1:
        board[nx][ny] = 0
        
    x, y = nx, ny
    
    if cur_time in dic:
        d = turn(d, dic[cur_time])

# 끝나는 시간
print(cur_time)
from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

R, C = map(int, input().split())
miro1, miro2 = [], []
for i in range(R):
    lst = list(input())
    miro1.append(lst[:])
    miro2.append(lst[:])
        

que1 = deque() # 불
que2 = deque() # 지훈
for i in range(R):
    for j in range(C):
        if miro1[i][j] == 'F':
            miro1[i][j] = 0
            miro2[i][j] = '.'
            que1.append((i, j, 0))
        elif miro1[i][j] == 'J':
            miro1[i][j] = '.'
            miro2[i][j] = 0
            que2.append((i, j, 0))
            
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 불
while que1:
    x, y, time = que1.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= R or ny < 0 or ny >= C: continue
        if miro1[nx][ny] == '#' or miro1[nx][ny] == 'F': continue
        if miro1[nx][ny] == '.':
            miro1[nx][ny] = time + 1
            que1.append((nx, ny, time + 1))

out_time = 1000001
while que2:
    x, y, time = que2.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            if time + 1 < out_time:
                out_time = time + 1
                out_x, out_y = x, y
            continue
        if miro2[nx][ny] == '#' or miro2[nx][ny] == 'J': continue

        if miro2[nx][ny] == '.' and (miro1[nx][ny] == '.' or time + 1 < miro1[nx][ny]):
            miro2[nx][ny] = time + 1
            que2.append((nx, ny, time + 1))

if out_time == 1000001:
    print("IMPOSSIBLE")
else:
    if miro1[out_x][out_y] == '.' or miro1[out_x][out_y] > out_time - 1:
        print(out_time)
    else:
        print("IMPOSSIBLE")

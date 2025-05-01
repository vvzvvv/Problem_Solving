from collections import deque

xx = [-1, 1, 0, 0]
yy = [0, 0, -1, 1]
#keypad = [[0] * 3 for _ in range(4)]

def bfs(x, y, dx, dy):
    keypad = [[0] * 3 for _ in range(4)]
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        if x == dx and y == dy:
            return keypad[x][y]
        for i in range(4):
            nx = x + xx[i]
            ny = y + yy[i]
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 3:
                continue
            if keypad[nx][ny] == 0:
                keypad[nx][ny] = keypad[x][y] + 1
                queue.append((nx, ny))
    
def solution(numbers, hand):
    answer = ''
    d = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2), 0: (3, 1)}
    global lx, ly, rx, ry
    (lx, ly), (rx, ry) = (3, 0), (3, 2) 
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            lx, ly = d[i]
            answer += 'L'
        elif i == 3 or i == 6 or i == 9:
            rx, ry = d[i]
            answer += 'R'
        else:
            dx, dy = d[i] # 목적지
            rd = bfs(rx, ry, dx, dy)
            ld = bfs(lx, ly, dx, dy)
            if ld > rd :
                answer += 'R'
                rx, ry = dx, dy
            elif ld < rd :
                answer += 'L'
                lx, ly = dx, dy
            else:
                if hand == 'left':
                    answer += 'L'
                    lx, ly = dx, dy
                else:
                    answer += 'R'
                    rx, ry = dx, dy
    return answer
def check(x, y, way, num, park):
    if way == "N":
        for i in range(-1, -(num+1), -1):
            dx = x + i
            if dx < 0 or park[dx][y] == "X" : return x, y
        x -= num

    elif way == "S":       
        for i in range(1, num+1):
            dx = x + i
            if dx >= n or park[dx][y] == "X" : return x, y
        x += num
    
    elif way == "W":
        for i in range(-1, -(num+1), -1):
            dy = y + i
            if dy < 0 or park[x][dy] == "X" : return x, y
        y -= num
    
    elif way == "E":
        for i in range(1, num+1):
            dy = y + i
            if dy >= m or park[x][dy] == "X" : return x, y
        y += num
    
    return x, y

def solution(park, routes):
    global n
    global m
    n = len(park)
    m = len(park[0])
    for i in range(n):
        for j in range(m):
            if park[i][j] == "S": x, y = i, j

    for r in routes:
        way, num = r.split()
        num = int(num)
        x, y = check(x, y, way, num, park)
        
    return x, y
def solution(park, routes):
    answer = []
    n, m = len(park), len(park[0])
    
    for i in range(n):
        for j in range(m):
            if park[i][j] == "S":
                x, y = i, j
                
    way = {"E": (0, 1), "W": (0, -1), "S": (1, 0), "N": (-1, 0)}
    
    for route in routes:
        w, num = route.split()

        flag = True
        for i in range(1, int(num) + 1):
            nx, ny = x + (way[w][0] * i), y + (way[w][1] * i)
            if nx < 0 or nx >= n or ny < 0 or ny >= m or park[nx][ny] == "X":
                flag = False
                break
        
        if flag: x, y = nx, ny
            
    return [x, y]
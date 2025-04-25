def solution(n):
    answer = [[0] * n for _ in range(n)]
    num = 1
    x, y = 0, 0
    
    while num <= n*n:
        
        while (y != n) and answer[x][y] == 0:
            answer[x][y] = num
            y += 1
            num += 1
            
        y -= 1
        x += 1
        
        while (x != n) and answer[x][y] == 0:
            answer[x][y] = num
            x += 1
            num += 1
            
        x -= 1
        y -= 1
        
        while (y >= 0) and answer[x][y] == 0:
            answer[x][y] = num
            y -= 1
            num += 1
            
        y += 1
        x -= 1
        
        while (x >= 0) and answer[x][y] == 0:
            answer[x][y] = num
            x -= 1
            num += 1
            
        y += 1
        x += 1
        
    return answer

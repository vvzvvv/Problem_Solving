def solution(n):
    answer = [[-1 for _ in range(n)] for _ in range(n)]
    
    # 우, 하, 좌, 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    x, y, d = 0, -1, 0
    num = 1
    while num <= n * n:
        nx = x + dx[d]
        ny = y + dy[d]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny] != -1:
            d = (d + 1) % 4
        
        else:
            x, y = nx, ny
            answer[x][y] = num
            num += 1
        
    return answer
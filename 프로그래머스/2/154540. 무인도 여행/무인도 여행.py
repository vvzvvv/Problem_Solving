def solution(maps):
    answer = []
    row, col = len(maps), len(maps[0])
    
    visited = [[False] * col for _ in range(row)]

    def dfs(x, y):
        stack = [(x, y)]
        food = 0
        
        while stack:
            cx, cy = stack.pop()
            
            if visited[cx][cy]:
                continue
            
            visited[cx][cy] = True
            food += int(maps[cx][cy])
            
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = cx+dx, cy+dy
                if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and maps[nx][ny] != "X":
                    stack.append((nx, ny))
        return food
            
    for i in range(row):
        for j in range(col):
            if maps[i][j] != "X" and visited[i][j] == False:
                res = dfs(i, j)
                if res: answer.append(res)
    answer.sort()
    
    if not answer: return [-1]
    return answer
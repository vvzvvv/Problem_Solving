import sys 
sys.setrecursionlimit(10000)

def solution(maps):
    answer = []
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    
    def dfs(x, y):
        if not (0 <= x < n and 0 <= y < m) or maps[x][y] == 'X' or visited[x][y]:
            return 0
        
        visited[x][y] = 1
        return int(maps[x][y]) + dfs(x-1, y) + dfs(x+1, y) + dfs(x, y-1) + dfs(x, y+1)
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(dfs(i, j))
    
    if not answer: return [-1]
    return sorted(answer)
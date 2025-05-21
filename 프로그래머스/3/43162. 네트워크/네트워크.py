def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(v):
        visited[v] = True
        for y in range(n):
            if computers[v][y] == 1 and not visited[y]:
                dfs(y)
    
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if computers[i][j] == 1 and not visited[j]:
                dfs(j)
                answer += 1
    
    answer += visited.count(False)
    return answer
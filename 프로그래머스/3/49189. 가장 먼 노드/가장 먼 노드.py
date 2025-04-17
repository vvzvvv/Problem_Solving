from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    distance = 1
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[v] + 1

        distance += 1
    
def solution(n, vertex):
    answer = 0
    graph = [[] for i in range(n+1)]
    
    for v in vertex:
        i, j = v[0], v[1]
        graph[i].append(j)
        graph[j].append(i)

    visited = [0] * (n + 1)

    bfs(graph, 1, visited)  
    
    max_distance = max(visited)
    answer = visited.count(max_distance)
    
    return answer
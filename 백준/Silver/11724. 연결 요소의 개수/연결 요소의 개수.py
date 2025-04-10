import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

n, m = map(int, input().split())

visited = [False] * (n + 1)

connected = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)
        
def dfs(graph, start, visited):
    if visited[start] == True: return False
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
    return True

result = 0
for i in range(1, n+1):
    if dfs(connected, i, visited) == True:
        result += 1

print(result)
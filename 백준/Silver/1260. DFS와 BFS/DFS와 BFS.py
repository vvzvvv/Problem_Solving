from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    r, c = map(int, input().split())
    graph[r].append(c)
    graph[c].append(r)

for g in graph:
    g.sort()

visited = [False] * (n + 1)
stack = []

def dfs(node):
    stack.append(node)
    print(node, end=' ')
    visited[node] = True
    
    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(nxt)
    stack.pop()

dfs(v)
print()

# === bfs ===
visited = [False] * (n + 1)

que = deque([v])
visited[v] = True
while que:
    node = que.popleft()
    print(node, end= ' ')
    for nxt in graph[node]:
        if not visited[nxt]:
            que.append(nxt)
            visited[nxt] = True

com = int(input())
graph = [[] for _ in range(com+1)]
visited = [0] * (com+1)

n = int(input())
for _ in range(n):
    frm, to = map(int, input().split())
    graph[frm].append(to)
    graph[to].append(frm)
    
def dfs(start):
    visited[start] = 1
    for node in graph[start]:
        if not visited[node]:
            dfs(node)

dfs(1)
print(sum(visited)-1)

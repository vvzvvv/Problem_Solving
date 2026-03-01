n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)
visited[1] = 1
result = 0
for f in graph[1]:
    if not visited[f]:
        visited[f] = 1
        result += 1
        
    for f_of_f in graph[f]:
        if not visited[f_of_f]:
            visited[f_of_f] = 1
            result += 1

print(result)
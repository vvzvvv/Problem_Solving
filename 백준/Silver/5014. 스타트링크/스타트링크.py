from collections import deque

n, start, goal, up, down = map(int, input().split())
visited = [-1] * (n + 1)
que = deque()
que.append(start)
visited[start] = 0

while que:
    x = que.popleft()
    
    if x == goal:
        print(visited[x])
        exit()
    for dx in (up, -down):
        nx = x + dx
        if nx < 1 or nx > n: continue
        if visited[nx] != -1: continue 
        que.append(nx)
        visited[nx] = visited[x] + 1
    
else:
    print("use the stairs")
    
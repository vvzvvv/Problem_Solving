from collections import deque

n, k = map(int, input().split())
visited = [-1] * 100001
queue = deque()
queue.append(n)
visited[n] = 0

while queue:
    cur = queue.popleft()
    if cur == k:
        break
    for i in (cur - 1, cur + 1, cur * 2):
        if i < 0 or i > 100000: continue
        if visited[i] != -1: continue
        visited[i] = visited[cur] + 1
        queue.append(i)
        
print(visited[k])
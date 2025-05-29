from collections import deque

begin, target = map(int, input().split())
visited = [-1] * 100001
cnt = 0
visited[begin] = 0
que = deque()
que.append((begin, 0))

while que:
    pos, sec = que.popleft()
    if pos == target:
        cnt += 1
    
    for move in (pos - 1, pos + 1, pos * 2):
        if move < 0 or move > 100000:
            continue
        if visited[move] == -1:
            que.append((move, sec + 1))
            visited[move] = sec + 1
        elif sec + 1 == visited[move]:
            que.append((move, sec + 1))

print(visited[target])
print(cnt)

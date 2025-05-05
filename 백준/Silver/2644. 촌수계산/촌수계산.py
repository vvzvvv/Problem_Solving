from collections import deque

people = int(input())
s, e = map(int, input().split())

one_chon = int(input()) # 부모 자식 관계 개수
graph = [[] for i in range(people + 1) ]

for i in range(one_chon):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)

def bfs(start, end):
    visited = [0] * (people + 1)
    queue = deque([start])
    visited[start] = 0
    
    while queue:
        v = queue.popleft()
        if v == end:
            return visited[v]
            
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[v] + 1

result = bfs(s, e)

if result == None: print(-1)
else: print(result)

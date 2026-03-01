n = int(input())
target = int(input())
visited = [[0] * n for _ in range(n)]

# 위 오 아 왼
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dis = 1
cnt = 1

x, y = n // 2, n // 2
visited[x][y] = cnt
idx = 0

answer = [x + 1, y + 1]
flag = True
while flag:
    
    for _ in range(2):
        for _ in range(dis):
            x += dx[(idx + 4) % 4]
            y += dy[(idx + 4) % 4]
            
            if x < 0 or x >= n or y < 0 or y >= n or visited[x][y]:
                flag = False
                break
            
            cnt += 1
            visited[x][y] = cnt
            
            if cnt == target:
                answer =[x + 1, y + 1]
        idx += 1
    
    dis += 1

for v in visited:
    print(*v)
print(*answer)
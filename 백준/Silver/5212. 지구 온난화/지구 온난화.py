r, c = map(int, input().split())
maps = []

for _ in range(r):
    maps.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 체크 함수: 바다 인접 수 체크
def check(x, y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >=c or maps[nx][ny] == '.':
            cnt += 1
    
    if cnt >= 3: # 인접 칸이 세 칸 이상이면 True
        return True
    else:
        return False


# 바다 인접 칸 체크 & 사라질 섬 리스팅
islands = []
for i in range(r):
    for j in range(c):
        if maps[i][j] == 'X' and check(i, j):
            islands.append((i, j))

# 사라질 섬들 변경
for x, y in islands:
    maps[x][y] = '.'

# 출력 범위 정하기
min_x, min_y = r, c
max_x, max_y = 0, 0
for x in range(r):
    for y in range(c):
        if maps[x][y] == 'X':
            if x < min_x:
                min_x = x
            if y < min_y:
                min_y = y
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y

# 최종 지도 출력
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        print(maps[x][y], end='')
    print()
        
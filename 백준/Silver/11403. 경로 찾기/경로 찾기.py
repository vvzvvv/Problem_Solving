n = int(input())
board = []

for i in range(n):
    board.append(list(map(int, input().split())))
    
def dfs(x, y):
    visited[y] = True
    for j in range(n):
        if board[y][j] == 1 and not visited[j]:
            board[x][j] = 1
            dfs(x,j)

for x in range(n):
    visited = [False] * n
    for y in range(n):
        if board[x][y] == 1 and not visited[x]:
            dfs(x, y)

for x in range(n):
    for y in range(n):
        print(board[x][y], end=' ')
    print()
    
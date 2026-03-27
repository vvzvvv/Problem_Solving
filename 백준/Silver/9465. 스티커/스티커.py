t = int(input())
for _ in range(t):
    n = int(input())
    board = []
    for _ in range(2):
        board.append(list(map(int, input().split())))
    
    if n >= 2:
        board[0][1] += board[1][0]
        board[1][1] += board[0][0]
    
    if n >= 3:
        for j in range(2, n):
            for i in range(2):
                if i == 0:
                    board[i][j] += max(board[0][j-2], board[1][j-2], board[1][j-1])
                elif i == 1:
                    board[i][j] += max(board[0][j-2], board[1][j-2], board[0][j-1])
    
    print(max(board[0][n-1], board[1][n-1]))
def solution(board):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    result = 0
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1: # 폭탄이면 주위 다 폭탄으로 만들기
                for k in range(8):
                    x = i + dx[k]
                    y = j + dy[k]
                    if x >= 0 and x <= n-1 and y >= 0 and y <= n-1 and board[x][y] == 0:
                        board[x][y] = 2
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                result += 1
                
    return result
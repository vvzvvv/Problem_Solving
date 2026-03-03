t = int(input())

def turn():
    arr_1, arr_2, arr_3, arr_4 = [], [], [], []
    temp = []
    for i in range(n):
        arr_1.append(board[i][i]) # \
        arr_2.append(board[i][n//2]) # |
        arr_3.append(board[i][n-1-i]) # /
        arr_4.append(board[n//2][i]) # -
        
    for i in range(n):
        board[i][n//2] = arr_1[i]
        board[i][n-1-i] = arr_2[i]
        board[n//2][n-1-i] = arr_3[i]
        board[i][i] = arr_4[i]
    
for _ in range(t):
    n, d = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    
    d = (d + 360) % 360
    moves = d // 45
    
    for _ in range(moves):
        turn()
    
    for b in board:
        print(*b)
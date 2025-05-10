import math

def solution(n, w, num):
    h = math.ceil(n / w)
    board = [[0] * w for _ in range(h)]
    
    cnt = 0
    flag = True
    for row in range(h):
        if row % 2 == 0:
            for col in range(w):
                cnt += 1
                board[row][col] = cnt
                
                if cnt == num:
                    now_row = row
                    now_col = col
                    
                if cnt == n:
                    flag = False
                    break
                    
        else:
            for col in range(w-1, -1, -1):
                cnt += 1
                board[row][col] = cnt
                
                if cnt == num:
                    now_row = row
                    now_col = col
                
                if cnt == n:
                    flag = False
                    break
        if not flag:
            break
            
    result = 0
    for i in range(now_row, h):
        if board[i][now_col] != 0:
            result += 1
    return result
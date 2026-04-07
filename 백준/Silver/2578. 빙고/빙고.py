board = [list(map(int, input().split())) for _ in range(5)]

def bingo():
    bingo_cnt = 0
    # 세로 확인
    for y in range(5):
        cnt = 0
        for x in range(5):
           cnt += board[x][y]
        if cnt == -5: bingo_cnt += 1
            
    # 가로 확인
    for x in range(5):
        if sum(board[x]) == -5: bingo_cnt += 1
    
    # 대각선 확인
    cnt = 0
    for i in range(5):
        cnt += board[i][i]
    if cnt == -5: bingo_cnt += 1
    
    cnt = 0
    for i in range(5):
        cnt += board[i][4-i]
    if cnt == -5: bingo_cnt += 1
    
    if bingo_cnt >= 3:
        return True
    
    return False



def check(num, result):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                board[i][j] = -1
                if bingo():
                    print(result)
                    exit()


call = [list(map(int, input().split())) for _ in range(5)]
result = 0
for r in range(5):
    for c in range(5):
        result += 1
        check(call[r][c], result)
        
def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board]
    
    while 1:
        blocks = set()
        # 보드 돌면서 깨질 수 있는 블록 좌표 체크.
        for x in range(m):
            for y in range(n):
                if board[x][y] == '.': continue
                temp = set()
                temp.add((x, y))
                for i, j in ((x, y+1), (x+1, y), (x+1, y+1)):
                    if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != board[x][y]:
                        temp.clear()
                        break                
                    temp.add((i, j))
                blocks.update(temp)

        # 깨지는 좌표 개수 추가하고,
        if len(blocks) == 0:
            break
        answer += len(blocks)
        
        # 깨지는 좌표는 '.' 로 변경
        for x, y in blocks:
            board[x][y] = '.'

        # 보드 재정비. 블록 돌면서(x+1)이 '.'면 x 축 변경. 최종 좌표에 현재 값 넣고, 원래 위치는 '.'
        for y in range(n):
            for x in range(m - 2, -1, -1):  # 아래에서 두 번째 줄부터 위로
                if board[x][y] != '.':
                    dx = x
                    while dx + 1 < m and board[dx + 1][y] == '.':
                        board[dx + 1][y] = board[dx][y]
                        board[dx][y] = '.'
                        dx += 1
                        
    return answer
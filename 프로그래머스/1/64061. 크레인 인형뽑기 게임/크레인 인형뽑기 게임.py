stack = []
result = 0

def keep(num):
    global result

    if not stack: stack.append(num)
    elif num == stack[-1]:
        stack.pop()
        result += 2
    else:
        stack.append(num)

def solution(board, moves):
    for y in moves:
        x = 0
        doll = 0
        while x != len(board):
            if board[x][y-1] != 0:
                doll = board[x][y-1]
                keep(doll)
                board[x][y-1] = 0
                break
            else:
                x += 1
    return result
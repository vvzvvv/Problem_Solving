n = int(input())
board = [0] * (367)
for _ in range(n):
    s, e = map(int, input().split())
    for i in range(s, e + 1):
        board[i] += 1

result = 0
col, row = 0, 0
for i in range(367):
    if board[i] == 0:
        result += col * row
        col, row = 0, 0
    else:
        if board[i] > row:
            row = board[i]
        col += 1

print(result)
from copy import deepcopy

t = int(input())

def func(n, board):
	temp_board = deepcopy(board)
	half = n // 2

	for i in range(n):
		# \ -> |
		temp_board[i][half] = board[i][i]
		# | -> /
		temp_board[i][n-1-i] = board[i][half]
		# / -> -
		temp_board[half][n-1-i] = board[i][n-1-i]
		# - -> \
		temp_board[i][i] = board[half][i]
	
	return temp_board

for _ in range(t):
	n, d = map(int, input().split())
	board = [list(map(int, input().split())) for _ in range(n)]

	d = (d + 360) % 360
	turns = d // 45

	for _ in range(turns):
		board = func(n, board)

	for b in board:
		print(*b)

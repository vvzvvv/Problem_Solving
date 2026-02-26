board = input()
n = len(board)

ch = board[0]
arr = []
for i in range(1, n):
    if ch[-1] == board[i]:
        ch += board[i]
    else:
        arr.append(ch)
        ch = board[i]
arr.append(ch)

result = ''
for a in arr:
    if a[0] == '.':
        result += a
    else:
        len_a = len(a)
        
        if len_a % 2 != 0:
            print(-1)
            exit()
        else:
            result += "AAAA" * (len_a // 4)
            result += "BB" * (len_a % 4 // 2) 
        
print(result)

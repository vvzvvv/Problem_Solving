arr = []
max_len = 0
for _ in range(5):
    word = input()
    arr.append(word)
    if len(word) > max_len: max_len = len(word) 

result = ''
for i in range(max_len):
    for j in range(5):
        try:
            result += arr[j][i]
        except: continue

print(result)
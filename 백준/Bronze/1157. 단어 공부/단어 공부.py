word = input()
word_low = word.lower() 
arr = [0] * 26

for i in word_low:
    index = ord(i) - 97
    arr[index] += 1

max_value = 0
for i in range(26):
    if max_value < arr[i]:
        max_value = arr[i]
        max_index = i

if arr.count(max_value) >= 2: print('?')
else:
    print(chr(max_index + 97).upper())
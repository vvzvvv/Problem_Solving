docs = input()
word = input()
n = len(word)
idx = 0
result = 0

while idx+n <= len(docs):
    if docs[idx:idx+n] == word:
        result += 1
        idx += n
    else:
        idx += 1

print(result)
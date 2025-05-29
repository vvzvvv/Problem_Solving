from collections import Counter

word = input()
count = Counter(word)

cnt_even = 0
mid = ''
for c in count:
    if count[c] % 2 == 1:
        mid = c
        cnt_even += 1
    
if cnt_even > 1:
    print("I'm Sorry Hansoo")
    exit()

count[mid] -= 1

result = ''
for c in sorted(count):
    if count[c] % 2 == 1:
        continue

    result += c * (count[c] // 2)
    
result_rev = reversed(result)
print(result + mid + ''.join(result_rev))

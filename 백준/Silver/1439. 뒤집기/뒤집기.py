s = list(map(int, input()))
cnt = [0, 0]
prev_num = s[0]

if 1 not in s or 0 not in s:
    print(0)
    exit()
    
for i in range(1, len(s)):
    if s[i] != prev_num:
        cnt[prev_num] += 1
        prev_num = s[i]
cnt[prev_num] += 1

print(min(cnt))
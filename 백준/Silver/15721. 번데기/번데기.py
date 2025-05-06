people = int(input())
time = int(input())
what = int(input()) # 0번 1데기

lst = []
zero_cnt, one_cnt = 0, 0 
n = 1
while one_cnt <= time:
    # bdg = abs(bdg - 1)
    for _ in range(2):
        lst.append(0)
        lst.append(1)
    zero_cnt += 2
    one_cnt += 2
    
    for _ in range(n+1):
        lst.append(0)
        zero_cnt += 1
    for _ in range(n+1):
        lst.append(1)
        one_cnt += 1
    n += 1
    
cnt = 0
for i in range(len(lst)):
    if lst[i] == what:
        cnt += 1
    if cnt == time:
        print(i % people)
        break
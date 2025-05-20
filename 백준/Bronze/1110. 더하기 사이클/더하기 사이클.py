original_number = input()
cnt = 0
number = original_number
# 0 보다 작으면 앞에 0 붙여서 두자리 수로 만듦
if int(number) < 10:
    number = '0' + number

cnt = 0
while 1:
    old_right = number[-1]
    n = 0
    for i in number:
        n += int(i)
    new_right = str(n)[-1]
    
    number = old_right + new_right
    cnt += 1
    
    if int(original_number) == int(number):
        print(cnt)
        break
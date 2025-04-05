m = int(input())
n = int(input())
arr = []

add_value = 0
min_value = 10000

for i in range(m, n+1): #m~n
    num = 0
    for j in range(1, i+1): #1~i
        if i % j == 0: num += 1 # 나눠지면 약수 개수 증가
    
    # i가 소수면(약수 2개), 소수합에 +, 최솟값 체크
    if num == 2:
        add_value += i
        if add_value < min_value:
            min_value = add_value

if add_value == 0: print(-1)
else:
    print(add_value)
    print(min_value)
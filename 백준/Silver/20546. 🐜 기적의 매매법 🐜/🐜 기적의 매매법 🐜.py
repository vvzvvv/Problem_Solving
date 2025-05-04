money = int(input())
lst = list(map(int, input().split()))

# 준현
j_money = money
stocks = 0

for price in lst:
    if j_money >= price:
        stocks += j_money // price
        j_money %= price
    
junhyeon = j_money + stocks * lst[-1]

# 성민
s_money = money
stocks = 0
prev_price = lst[0]
cnt_up = 0
cnt_down = 0

for i in range(1, len(lst)-1):
    if lst[i] > prev_price:
        prev_price = lst[i]
        cnt_up += 1
        cnt_down = 0
    elif lst[i] < prev_price:
        prev_price = lst[i]
        cnt_down += 1
        cnt_up = 0
    else :
        cnt_up, cnt_down = 0, 0
    # 3연 상승 - 전량 매도
    if cnt_up >= 3:
        if stocks:
            s_money = lst[i] * stocks
            stocks = 0
    # 3연 하락 - 전량 매수
    elif cnt_down >= 3 and s_money >= lst[i]:
        stocks += s_money // lst[i]
        s_money %= lst[i]
        
sungmin = s_money + stocks * lst[-1]

if junhyeon > sungmin:
    print("BNP")
elif junhyeon < sungmin:
    print("TIMING")
else:
    print("SAMESAME")
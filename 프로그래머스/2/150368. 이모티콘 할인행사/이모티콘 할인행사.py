from itertools import product

def solution(users, emoticons):
    n, m = len(users), len(emoticons)
    discounts = [10, 20, 30, 40]
    result_subs, result_total = 0, 0
    
    emo_prices = []
    for emo in emoticons:
        temp = []
        for d in discounts:
            temp.append(emo * (100 - d) // 100)
        emo_prices.append(temp)
    
    idx = {10: 0, 20: 1, 30: 2, 40: 3}
    
    for combs in list(product(discounts, repeat=m)):
        subs, total = 0, 0

        for u_rate, u_limit in users:
            u_total = 0
            for i in range(m):    
                if combs[i] >= u_rate:
                    p = idx[combs[i]]
                    u_total += emo_prices[i][p]
            
            if u_total >= u_limit:
                subs += 1
            else:
                total += u_total
        
        if subs > result_subs:
            result_subs, result_total = subs, total
        elif subs == result_subs:
            if total > result_total:
                result_total = total
    
    return [result_subs, result_total]

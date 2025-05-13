def solution(s):
    answer = [0, 0]
    while 1:
        zero_num = int(s.count('0'))
        n = len(s) - zero_num
        answer[1] += zero_num
    
        s = ''
        remain = 0
        
        while n > 0 :
            remain = n % 2
            n //= 2
            s += str(remain)
        
        s = s[::-1]
        answer[0] += 1
        
        if s == "1": break
    return answer
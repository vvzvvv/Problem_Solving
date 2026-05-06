def solution(storey):
    answer = 0
    
    while storey != 0:
        remainder = storey % 10
        
        if remainder > 5:
            answer += (10 - remainder)
            storey += (10 - remainder)
            
        elif remainder < 5:
            answer += remainder
            storey -= remainder
            
        elif remainder == 5:
            nxt_num = (storey // 10) % 10
            answer += remainder
            if nxt_num < 5:
                storey -= remainder
            else:
                storey += remainder      
        
        storey //= 10
    
    return answer
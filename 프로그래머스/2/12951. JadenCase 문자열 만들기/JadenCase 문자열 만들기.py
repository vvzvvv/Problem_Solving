def solution(s):
    answer = ''
    
    first = True
    for i in range(len(s)):
        if s[i] == ' ':
            answer += s[i]
            first = True
            continue
        
        # 공백 뒤 첫글자
        if first:
            answer += s[i].upper()
            first = False
                
        # 첫글자 아님
        else:
            answer += s[i].lower()
            
    return answer
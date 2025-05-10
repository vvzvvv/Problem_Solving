def solution(s):
    result = 0
    for i in range(len(s)):
        word = s[i:] + s[:i]
        stack = []
        flag = True
        
        for item in word:
            # 여는 괄호면 스택에 추가
            if item in ("[", "(", "{"):
                stack.append(item)
            
            # 닫는 괄호면 스택 팝이랑 짝인지 체크
            else:
                try:
                    last = stack.pop()
                except:
                    flag = False
                    break
                
                if last + item not in ("[]", "{}", "()"):
                    flag = False
                    break

        if flag and len(stack) == 0:
            result += 1
        
    return result
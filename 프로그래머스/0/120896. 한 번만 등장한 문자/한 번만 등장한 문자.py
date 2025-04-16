def solution(s):
    answer = ''
    data = [0] * 26
    for i in s:
        index = ord(i) - 97
        data[index] += 1
    
    for i in range(26):
        if data[i] == 1:
            answer += chr(i + 97)
        
    return answer
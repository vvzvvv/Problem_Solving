def solution(s):
    answer = []
    s = s[2:len(s)-2]
    lst = []
    
    for tup in s.split('},{'):
        temp = []
        for num in tup.split(','):
            temp.append(int(num))
        lst.append(temp)
        
    lst.sort(key=lambda x : len(x))
    
    for tup in lst:
        for item in tup:
            if item not in answer:
                answer.append(item)
    
    return answer
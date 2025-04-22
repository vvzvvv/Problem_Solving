def solution(name, yearning, photo):
    answer = []
    n = len(name)
    d = dict()
    for i in range(n):
        d[name[i]] = yearning[i]

    for i in range(len(photo)):
        result = 0
        for j in range(len(photo[i])):
            if photo[i][j] in d.keys():
                result += d[photo[i][j]]
            else: continue
        answer.append(result)
    
    return answer
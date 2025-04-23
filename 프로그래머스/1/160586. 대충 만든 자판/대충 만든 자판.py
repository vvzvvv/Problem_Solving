def solution(keymap, targets):
    answer = []
    d = dict()
    for k in keymap:
        for i in range(len(k)):
            if k[i] not in d.keys():
                d[k[i]] = i + 1
            elif d[k[i]] > i + 1:
                d[k[i]] = i + 1
    for i in range(len(targets)):
        result = 0
        for j in range(len(targets[i])):
            if targets[i][j] not in d.keys():
                answer.append(-1)
                break
            result += d[targets[i][j]]
            if j == len(targets[i]) - 1: answer.append(result)
    
    return answer
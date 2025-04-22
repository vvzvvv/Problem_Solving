def solution(array):
    d = dict()
    for i in array:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] += 1
    
    max_value = max(d.values())
    if list(d.values()).count(max_value) > 1:
        return -1
    else:
        for k, v in d.items():
            if v == max_value:
                return k

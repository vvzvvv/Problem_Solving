def solution(X, Y):
    answer = ''
    xi = {}
    yi = {}
    for ch in X:
        if ch not in xi:
            xi[ch] = 1
        else: xi[ch] += 1
    for ch in Y:
        if ch not in yi:
            yi[ch] = 1
        else: yi[ch] += 1
    
    d = {}
    for num, cnt in xi.items():
        if num in yi: 
            d[num] = min(xi[num], yi[num])

    if not d: return "-1"
    elif len(d) == 1 and '0' in d: return "0"

    for i in range(9, -1, -1):
        if str(i) in d:
            print(i)
            for _ in range(d[str(i)]):
                answer += str(i)
    
    return answer
    
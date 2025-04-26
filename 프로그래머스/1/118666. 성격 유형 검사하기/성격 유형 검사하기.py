def solution(survey, choices):
    지표 = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    d = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    n = len(survey)
    for i in range(n):
        if choices[i] >= 5:
            d[survey[i][1]] += choices[i] - 4
        elif choices[i] <= 3:
            d[survey[i][0]] += abs(choices[i] - 4)
    
    result = []
    for i, j in 지표:
        if d[i] >= d[j] : result.append(i)
        else: result.append(j)
    answer = ''.join(result)
    
    return answer
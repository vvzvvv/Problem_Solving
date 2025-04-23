def solution(n, m, section):
    wall = dict()
    for k, v in enumerate([1] * n):
        wall[k+1] = v
    for s in section:
        wall[s] = 0
    result = 0
    for s in section:
        if wall[s] == 0:
            for i in range(m):
                wall[s+i] = 1
            result += 1
    return result
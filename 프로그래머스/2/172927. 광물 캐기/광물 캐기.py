def solution(picks, minerals):
    n = sum(picks)
    if len(minerals) > n * 5: minerals = minerals[:n*5]
    
    fatigue = [
        [1, 1, 1],
        [5, 1, 1],
        [25, 5, 1]
    ]
    
    wei_mines = []
    for i in range(0, len(minerals), 5):
        mines = minerals[i:i+5]
        weight = 0
        for m in mines:
            if m == "diamond": weight += 25
            elif m == "iron": weight += 5
            else: weight += 1
        wei_mines.append([weight, mines])
    wei_mines.sort(key=lambda x: x[0], reverse=True)
    
    result = 0
    for wei, mines in wei_mines:
        if picks[0]:
            picks[0] -= 1
            pick = 0
        elif picks[1]:
            picks[1] -= 1
            pick = 1
        elif picks[2]:
            picks[2] -= 1
            pick = 2
        
        for m in mines:
            if m == "diamond":
                result += fatigue[pick][0]
            elif m == "iron":
                result += fatigue[pick][1]
            else:
                result += 1
    return result
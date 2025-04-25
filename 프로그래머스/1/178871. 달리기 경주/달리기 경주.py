def solution(players, callings):
    d = {}
    di = {}
    for i, player in enumerate(players):
        d[player] = i
        di[i] = player
        
    for call in callings: 
        call_num = d[call]
        prev_num = call_num - 1
        prev_name = di[prev_num]
        
        d[call], d[prev_name] = prev_num, call_num
        di[prev_num], di[call_num] = call, prev_name
        
    result = [0] * len(players)
    for k, v in d.items():
        result[v] = k
    return result
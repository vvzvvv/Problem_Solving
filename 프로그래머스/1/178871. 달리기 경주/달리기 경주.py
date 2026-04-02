def solution(players, callings):
    d1, d2 = {}, {}
    
    for rank, player in enumerate(players):
        d1[rank] = player
        d2[player] = rank
    for now in callings:
        now_rank = d2[now]
        prev = d1[now_rank - 1]
        prev_rank = d2[prev]
        d1[prev_rank], d1[now_rank] = now, prev
        d2[now] -= 1
        d2[prev] += 1

    sorted(d1)
    return list(d1.values())
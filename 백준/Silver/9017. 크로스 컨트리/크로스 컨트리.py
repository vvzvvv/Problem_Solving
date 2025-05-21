T = int(input())
for _ in range(T):
    N = int(input())
    lst = [int(x) for x in input().split()]
    out = set()
    for i in range(1, max(lst)+1):
        if lst.count(i) < 6:
            out.add(i)
    
    lst = [x for x in lst if x not in out]
    
    d = {}
    for i in range(len(lst)):
        if lst[i] not in d:
            d[lst[i]] = [i + 1]
        else:
            d[lst[i]].append(i + 1)
    
    rank = {}
    for k, v in d.items():
        rank[k] = sum(v[0:4])
    
    min_value = min(rank.values())
    
    if list(rank.values()).count(min_value) > 1:
        min_v = 1001
        for k, v in d.items():
            if rank[k] == min_value:
                if v[4] < min_v:
                    min_v = v[4]
                    team = k
        print(team)
    
    else:
        for k, v in rank.items():
            if v == min_value:
                print(k)
                break
    
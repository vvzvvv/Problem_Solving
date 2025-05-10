def solution(friends, gifts):
    df = {}
    for idx, f in enumerate(friends):
        df[f] = idx  # 무지: 0 , 라이언: 1 
    
    board = [[0] * len(friends) for _ in range(len(friends))]
    indicator = [0] * len(friends)
    
    for gift in gifts:
        a, b = gift.split(' ')
        board[df[a]][df[b]] += 1    
        # 선물지수 계산
        indicator[df[a]] += 1
        indicator[df[b]] -= 1
    
    result = [0] * len(friends)
    for a in range(len(friends)):
        for b in range(len(friends)):
            if a == b: continue
            
            # 주고받은 기록 있고, 
            if board[a][b] > board[b][a]:
                result[a] += 1
            
            # 기록 같거나 / 기록 X 
            elif board[a][b] == board[b][a]:
                # 선물 지수 큰 사람이 작은 사람에게 받음 (선물지수 = 친구들에게 준 수 - 받은 수)
                if indicator[a] > indicator[b]:
                    result[a] += 1
                #선물지수 같다면 다음달에 선물 X
                
    return max(result)
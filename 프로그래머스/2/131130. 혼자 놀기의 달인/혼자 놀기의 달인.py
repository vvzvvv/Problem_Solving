
def solution(cards):
    groups = []
    n = len(cards)
    visited = [0] * n
    
    def grouped(box_num, cnt):
        if visited[box_num]: return cnt
        visited[box_num] = 1
        return grouped(cards[box_num] - 1, cnt + 1)
                
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            groups.append(grouped(cards[i] - 1, 1))
    
    if 0 in groups or n in groups: return 0
    
    groups.sort()
    return groups[-1] * groups[-2]
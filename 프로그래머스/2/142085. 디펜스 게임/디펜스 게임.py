import heapq

def solution(n, k, enemy):
    if k >= len(enemy): return len(enemy)

    answer = 0
    h = []
    cnt_n = 0
    
    for e in enemy:
        cnt_n += e
        
        if k == 0 and cnt_n > n: break
        
        heapq.heappush(h, -e)
            
        if cnt_n > n:
            max_v = -heapq.heappop(h)
            cnt_n -= max_v
            k -= 1
            answer += 1
    
    return answer + len(h)
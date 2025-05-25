from heapq import heapify, heappush, heappop

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    n = len(scoville)
    while any(x for x in scoville if x < K):
        if answer == n - 1 :
            return -1

        a, b = heappop(scoville), heappop(scoville)
        heappush(scoville, a + b * 2)
        answer += 1
    
    
    return answer
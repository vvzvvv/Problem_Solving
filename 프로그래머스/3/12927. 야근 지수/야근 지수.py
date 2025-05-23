from heapq import heappush, heappop

def solution(n, works):
    answer = 0
    h = []
    for w in works:
        heappush(h, -w)
    
    for _ in range(n):
        if all(x == 0 for x in h): break
        num = heappop(h)
        heappush(h, num + 1)
    
    return sum([i*i for i in h])
import heapq

def solution(operations):
    h = []
    
    for operation in operations:
        op, value = operation.split()
        if op == 'I':
            heapq.heappush(h, int(value))
            
        elif operation == 'D 1' and len(h):
            h.remove(max(h))
            
        elif operation == 'D -1' and len(h):
            heapq.heappop(h)
    
    if not len(h):
        return [0, 0]
    
    return [max(h), min(h)]
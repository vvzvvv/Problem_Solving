import math

def solution(k, d):
    result = 0
    x = 0
    
    while x <= d:
        y = math.isqrt(d ** 2 - x ** 2)
        result += (y // k) + 1
        x += k
        
    return result
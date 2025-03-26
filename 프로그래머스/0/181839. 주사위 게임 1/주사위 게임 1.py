def solution(a, b):
    if a % 2 != 0 and b % 2 != 0:
        result = a*a + b*b
    elif a % 2 != 0 or b % 2 != 0:
        result = 2 * (a + b)
    else:
        result = abs(a-b)
    
    return result
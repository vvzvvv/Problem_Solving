n, r, c = map(int, input().split())

def z(n, r, c):
    if n == 0:
        return 0
        
    half = 2 ** (n - 1)
    size = half * half
    
    if r < 2 ** (n - 1) and c < 2 ** (n - 1):
        return z(n - 1,  r, c)
    elif r < 2 ** (n - 1) and c >= 2 ** (n - 1):
        return size + z(n - 1, r, c - half)
    elif r >= 2 ** (n - 1) and c < 2 ** (n - 1):
        return 2 * size + z(n - 1, r - half, c)
    else:
        return 3 * size + z(n - 1, r - half, c - half)
    
print(z(n, r, c))
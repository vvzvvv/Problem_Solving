def solution(numbers, hand):
    answer = ''
    dic = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        0: (3, 1)
    }
    
    lx, ly = 3, 0
    rx, ry = 3, 2
    
    for num in numbers:
        if num in (1, 4, 7):
            lx, ly = dic[num]
            answer += 'L'
        elif num in (3, 6, 9):
            rx, ry = dic[num]
            answer += 'R'
        elif num in (2, 5, 8, 0):
            nx, ny = dic[num]
            ld = abs(nx - lx) + abs(ny - ly)
            rd = abs(nx - rx) + abs(ny - ry)
            
            if ld > rd:
                rx, ry = nx, ny
                answer += 'R'
            elif ld < rd:
                lx, ly = nx, ny
                answer += 'L'
            elif ld == rd:
                if hand == 'right':
                    rx, ry = nx, ny
                    answer += 'R'
                else:
                    lx, ly = nx, ny
                    answer += 'L'
    return answer
def solution(wallpaper):
    min_x, max_x = 50, 0
    min_y, max_y = 50, 0
    n, m = len(wallpaper), len(wallpaper[0])
    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == "#":
                if i < min_x: min_x = i
                if i > max_x: max_x = i
                if j < min_y: min_y = j
                if j > max_y: max_y = j
    
    return min_x, min_y, max_x + 1, max_y + 1
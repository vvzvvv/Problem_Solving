left = {
    "q": (0, 0),
    "w": (0, 1),
    "e": (0, 2),
    "r": (0, 3),
    "t": (0, 4),
    "a": (1, 0),
    "s": (1, 1),
    "d": (1, 2),
    "f": (1, 3),
    "g": (1, 4),
    "z": (2, 0),
    "x": (2, 1),
    "c": (2, 2),
    "v": (2, 3)
}

right = {
    "y": (0, 1),
    "u": (0, 2),
    "i": (0, 3),
    "o": (0, 4),
    "p": (0, 5),
    "h": (1, 1),
    "j": (1, 2),
    "k": (1, 3),
    "l": (1, 4),
    "b": (2, 0),
    "n": (2, 1),
    "m": (2, 2)
}

l, r = input().split()
word = input()

result = 0
lx, ly = left[l]
rx, ry = right[r]
for ch in word:
    if ch in left:
        dx, dy = left[ch]
        result += abs(lx - dx) + abs(ly - dy)
        lx, ly = dx, dy
    elif ch in right:
        dx, dy = right[ch]
        result += abs(rx - dx) + abs(ry - dy)
        rx, ry = dx, dy
    result += 1
    
print(result)
k = int(input())
way, size = [], []
for _ in range(6):
    w, s = map(int, input().split())
    way.append(w)
    size.append(s)
way += way
size += size

w, h = 0, 0
for i in range(len(way)):
    if way[i] in (1, 2):
        if size[i] > w:
            w = size[i]
    elif way[i] in (3, 4):
        if size[i] > h:
            h = size[i]

for i in range(len(way)):
    if way[i:i+2] == way[i+2:i+4]:
        square = size[i+1] * size[i+2]
        break
        
print(((w * h) - square) * k)
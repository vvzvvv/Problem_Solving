h, w = map(int, input().split())
result = [[-1] * w for _ in range(h)]

weather = []
for _ in range(h):
    weather.append(input())

for x in range(len(weather)):
    for y in range(len(weather[0])):
        min = 0
        ny = y
        while ny >= 0:
            if weather[x][ny] == 'c':
                result[x][y] = min
                break
            ny -= 1
            min += 1

for x in range(len(weather)):
    for y in range(len(weather[0])):
        print(result[x][y], end=' ')
    print()
n = int(input())
score = {1 : 0, 2 : 0}
result = {0 : 0, 1 : 0, 2 : 0}
winner = 0
start = "00:00"

def toSec(time):
    m, s = time.split(':')
    return int(m) * 60 + int(s)
    
for _ in range(n):
    team, time = input().split()
    score[int(team)] += 1

    if score[1] > score[2]:
        if winner != 1:
            result[winner] += toSec(time) - toSec(start)
            start = time
            winner = 1
    elif score[2] > score[1]:
        if winner != 2:
            result[winner] += toSec(time) - toSec(start)
            start = time
            winner = 2
    else: # 동점
        result[winner] += toSec(time) - toSec(start)
        start = time
        winner = 0

result[winner] += toSec("48:00") - toSec(start)

for i, v in result.items():
    m = result[i] // 60
    s = result[i] % 60
    result[i] = f"{m:02}:{s:02}"

print(result[1])
print(result[2])
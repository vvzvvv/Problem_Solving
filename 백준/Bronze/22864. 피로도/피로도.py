a, b, c, m = map(int, input().split())
fatigue, work = 0, 0

for _ in range(24):
    if fatigue + a <= m:
        work += b
        fatigue += a
    else:
        fatigue -= c
        if fatigue < 0:
            fatigue = 0

print(work)
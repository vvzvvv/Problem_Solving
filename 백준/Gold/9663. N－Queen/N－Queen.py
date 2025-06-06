n = int(input())
queens = []
cnt = 0
visited1= [0] * n
visited2 = [0] * (2 * n - 1)
visited3 = [0] * (2 * n - 1)

def func(x): # 현재 x 축에 퀸 배치
    global cnt
    if x == n:
        cnt += 1
        return
    for y in range(n):
        if visited1[y] or visited2[x+y] or visited3[x-y+n-1]:
            continue
        visited1[y] = 1
        visited2[x+y] = 1
        visited3[x-y+n-1] = 1
        func(x + 1)
        visited1[y] = 0
        visited2[x+y] = 0
        visited3[x-y+n-1] = 0

func(0)
print(cnt)
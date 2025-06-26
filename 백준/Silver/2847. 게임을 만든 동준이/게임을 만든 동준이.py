n = int(input())

score = []
for _ in range(n):
    score.append(int(input()))

cnt = 0
for i in range(n-2, -1, -1):
    while score[i] >= score[i+1]:
        score[i] -= 1
        cnt += 1
print(cnt)


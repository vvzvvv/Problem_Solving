n = int(input())
dp = [0] * max(4, n + 1)
dp[2], dp[3] = 1, 1
path = [0] * max(4, n + 1)
path[2], path[3] = 1, 1

for i in range(4, n+1):
    dp[i] = dp[i-1] + 1
    path[i] = i-1
    if i % 3 == 0 and dp[i//3] + 1 < dp[i]:
        dp[i] = dp[i//3] + 1
        path[i] = i // 3
    if i % 2 == 0 and dp[i//2] + 1 < dp[i]:
        dp[i] = dp[i//2] + 1
        path[i] = i // 2

print(dp[n])

cur = n
while 1:
    print(cur, end=' ')
    if cur == 1: break
    cur = path[cur]

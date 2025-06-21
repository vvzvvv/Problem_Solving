n = int(input())
fee = [[0,0,0]]

for _ in range(n):
    fee.append(list(map(int, input().split())))

dp = [[0,0,0] for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + fee[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + fee[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + fee[i][2]
print(min(dp[n]))
            
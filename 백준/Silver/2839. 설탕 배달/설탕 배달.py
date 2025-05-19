n = int(input()) 
dp = [-1] * (n + 1)
# dp[3], dp[5] = 1, 1

for i in range(3, n+1):
    if i == 3 or i == 5:
        dp[i] = 1
    elif dp[i-3] == -1 and dp[i-5] == -1:
        continue
    elif dp[i-3] == -1:
        dp[i] = dp[i-5] + 1
    elif dp[i-5] == -1:
        dp[i] = dp[i-3] + 1
    else:    
        dp[i] = min(dp[i-3] + 1, dp[i-5] + 1)
print(dp[n])
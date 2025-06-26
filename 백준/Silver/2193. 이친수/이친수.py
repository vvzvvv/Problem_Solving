n = int(input())
dp = [[0, 0] for _ in range(91)]  

if n == 1:
    print(1)
    exit()
    
if n >= 2:
    dp[1] = [0, 1]
if n >= 3:
    dp[2] = [1, 0]
if n >= 4:
    for i in range(3, n):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]

result = dp[n-1][0] * 2 + dp[n-1][1]
print(result)


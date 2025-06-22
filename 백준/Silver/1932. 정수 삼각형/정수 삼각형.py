n = int(input())
arr = []
arr.append([0])
dp = []
dp.append([0])
for i in range(n):
    arr.append(list(map(int, input().split())))
    dp.append([0]*(i+1))

if n >= 1:
    dp[1] = arr[1]
if n >= 2:
    for i in range(2, n+1):
        for j in range(i):
            if j == 0:
                dp[i][j] = dp[i-1][j] + arr[i][j]
            elif j == i-1:
                dp[i][j] = dp[i-1][j-1] + arr[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j]
print(max(dp[n]))
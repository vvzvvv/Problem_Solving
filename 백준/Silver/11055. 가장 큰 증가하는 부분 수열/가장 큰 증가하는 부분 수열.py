n = int(input())
arr = list(map(int, input().split()))
total = 0
dp = [0] * n
maxval = 0

for i in range(n):
    dp[i] = arr[i]
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+ arr[i])
print(max(dp))
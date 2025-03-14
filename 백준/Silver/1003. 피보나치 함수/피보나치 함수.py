case = int(input())
case_list = []
#dp = [[0,0]] * 40
dp = [[0, 0] for _ in range(41)]
dp[0][0] = 1
dp[1][1] = 1

for _ in range(case):
  case_list.append(int(input()))

for n in range(2, 41):
  dp[n] = [x + y for x, y in zip(dp[n-1], dp[n-2])]

for i in case_list:
  a, b = dp[i]
  print(a, b)

n, k = map(int, input().split())
wallet = []
for _ in range(n):
    coin = int(input())
    if coin <= k:
        wallet.append(coin)
        
cnt = 0
idx = -1

while k != 0:
    if k // wallet[idx] > 0:
        cnt += (k // wallet[idx])
        k %= wallet[idx]
    else:
        idx -= 1

print(cnt)
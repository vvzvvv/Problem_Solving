import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

cnt_minus = [0] * 1000001
cnt_plus = [0] * 1000001
for i in range(n):
    num = int(input())
    if num >= 0:
        cnt_plus[num] += 1
    else:
        cnt_minus[-num] += 1

for i in range(1000000, -1, -1):
    if cnt_minus[i] > 0:
        for _ in range(cnt_minus[i]):
            print(-i)

for i in range(1000001):
    if cnt_plus[i] > 0:
        for _ in range(cnt_plus[i]):
            print(i)
   
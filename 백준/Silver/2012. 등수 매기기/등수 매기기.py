import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
rank = 1
result = 0
for i in range(n):
    result += abs(rank - arr[i])
    rank += 1
print(result)
import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split()) 
arr = [0]
for num in map(int, input().split()):
    arr.append(num + arr[-1])

for _ in range(M):
    i, j = map(int, input().split())
    print(arr[j] - arr[i-1])

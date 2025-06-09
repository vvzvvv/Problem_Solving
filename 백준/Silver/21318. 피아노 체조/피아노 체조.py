import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))
cnt_lst = [0] * n
prev_value = 0
cnt = 0
for i in range(n):
    if arr[i] < prev_value:
       cnt += 1
    cnt_lst[i] = cnt
    prev_value = arr[i]
cnt_lst[-1] = cnt

q = int(input())
for _ in range(q):
    x, y = map(int, input().split())
    print(cnt_lst[y-1] - cnt_lst[x-1])
    
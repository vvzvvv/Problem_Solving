import sys
lines = sys.stdin.readlines()

result = []
def func(k, arr, start):
    if len(result) == 6:
        print(*result)
        return
    for i in range(start, k):
        result.append(arr[i])
        func(k, arr, i+1)
        result.pop()

for line in lines:
    if line == '0': break
    arr = list(map(int, line.split()))
    k, arr = arr[0], arr[1:]
    func(k, arr, 0)
    print()
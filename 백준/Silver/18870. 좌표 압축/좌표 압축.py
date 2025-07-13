n = int(input())
arr = list(map(int, input().split()))

sorted_arr = sorted(set(arr))

def low_idx(target, length):
    st, en = 0, length
    while st < en:
        mid = (st + en) // 2
        if sorted_arr[mid] >= target:
            en = mid
        else:
            st = mid + 1
    return st

for i in range(n):
    print(low_idx(arr[i], len(sorted_arr)), end=' ')
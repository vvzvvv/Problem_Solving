L, C = map(int, input().split()) #15
arr = sorted(list(x for x in input() if x != ' '))
result = []

def func(depth, start):
    if depth == L:
        cnt1, cnt2 = 0, 0
        for ch in result:
            if ch in ('a', 'e', 'i', 'o', 'u'):
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt1 == 0: return
        if cnt2 < 2: return
        
        print(''.join(result))
        return
    for i in range(start, C):
        result.append(arr[i])
        func(depth + 1, i + 1)
        result.pop()

func(0, 0)
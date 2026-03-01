n, m = map(int, input().split())
path = [0] * m

def func(st, depth):
    if depth == m:
        print(*path)
        return

    for i in range(st, n + 1):
        path[depth] = i
        func(i, depth + 1)

func(1, 0)

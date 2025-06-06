n, m = map(int, input().split())
visited = [False] * (n + 1)
path = []

def tracking(depth):
    if depth == m:
        print(' '.join(map(str, path)))
        return
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            path.append(i)
            tracking(depth + 1)
            path.pop()
            visited[i] = False
    
tracking(0)

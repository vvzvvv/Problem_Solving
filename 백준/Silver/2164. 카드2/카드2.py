from collections import deque

n = int(input())
que = deque(list(range(1, n + 1)))

while len(que) != 1:
    que.popleft()
    num = que.popleft()
    que.append(num)

print(que.popleft())
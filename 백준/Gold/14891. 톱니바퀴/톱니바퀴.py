from collections import deque
import copy
gears = [[]]

for _ in range(4):
    gears.append(deque(list(map(int, input()))))

def turn(que, d):
    if d == 1:
        que.appendleft(que.pop())
    elif d == -1:
        que.append(que.popleft())

k = int(input())
for _ in range(k):
    num, d = map(int, input().split())
    turn_check = [0, 0, 0, 0, 0]
    turn_check[num] = d
    
    # 왼쪽 체크
    for i in range(num, 1, -1):
        if gears[i][6] != gears[i-1][2]:
            turn_check[i-1] = -turn_check[i]
        else:
            break
    
    # 오른쪽 체크
    for i in range(num, 4):
        if gears[i][2] != gears[i+1][6]:
            turn_check[i+1] = -turn_check[i]
        else:
            break
    
    # 회전 체크
    for i in range(1, 5):
        if turn_check[i] != 0:
            turn(gears[i], turn_check[i])
result = 0
for i in range(1, 5):
    result += gears[i][0] * (2 ** (i - 1))
print(result)

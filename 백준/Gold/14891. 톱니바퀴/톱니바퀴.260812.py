from collections import deque

wheels = [[]]
for _ in range(4):
	wheels.append(deque([int(num) for num in input()]))

k = int(input())

for _ in range(k):
	idx, dir = map(int, input().split()) # 톱니 번호, 방향 # 1 시계 -1 반시계

	turn = [0, 0, 0, 0, 0] # 시계 1, 반시계 -1, 안움직임 0
	turn[idx] = dir
	
	# 왼쪽 탐색
	for i in range(idx, 1, -1):
		if wheels[i-1][2] + wheels[i][6] != 1: break
		turn[i-1] = -turn[i]

	# 오른쪽 탐색
	for i in range(idx, 4):
		if wheels[i][2] + wheels[i+1][6] != 1: break
		turn[i+1] = -turn[i]


	# turn 체크해서 바퀴들 회전
	for i in range(1, 5):
		if turn[i] == 0: continue

		if turn[i] == 1: # 시계방향
			wheels[i].appendleft(wheels[i].pop())
		elif turn[i] == -1:
			wheels[i].append(wheels[i].popleft())

	
# 12시 방향들 합산해서 출력
result = sum(2 ** (i - 1) for i in range(1, 5) if wheels[i][0])
print(result)

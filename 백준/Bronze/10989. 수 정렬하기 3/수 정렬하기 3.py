import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
count = [0] * 10001

for _ in range(n):
    num = int(input())
    # 해당 번째의 등장횟수 추가
    count[num] += 1

for index in range(10001):
    # 등장 횟수가 0이 아니면
    if count[index] != 0:
        # 등장 횟수만큼
        time = count[index]
        for _ in range(time):
            # 인덱스 출력
            print(index)
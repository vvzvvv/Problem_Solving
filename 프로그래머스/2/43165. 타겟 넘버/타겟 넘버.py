from collections import deque

def solution(numbers, target):
    queue = deque()
    queue.append((0, 0))  # (현재 인덱스, 현재까지의 합)
    count = 0
  
    while queue:
        idx, total = queue.popleft()

        if idx == len(numbers):
            if total == target:
                count += 1
        else:
            queue.append((idx + 1, total + numbers[idx]))
            queue.append((idx + 1, total - numbers[idx]))

    return count

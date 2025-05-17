from collections import deque
def solution(queue1, queue2):
    answer = 0
    queue1, queue2 = deque(queue1), deque(queue2)
    n = len(queue1)
    total1, total2 = sum(queue1), sum(queue2)
    
    # if max(queue1) > (total1 + total2) / 2 or max(queue2) > (total1 + total2) / 2: return -1
    while total1 != total2:
        if total1 > total2:
            t = queue1.popleft()
            queue2.append(t)
            total2 += t
            total1 -= t
        elif total2 > total1:
            t = queue2.popleft()
            queue1.append(t)
            total1 += t
            total2 -= t

        answer += 1
        if answer == 4 * n:
            return -1
    return answer
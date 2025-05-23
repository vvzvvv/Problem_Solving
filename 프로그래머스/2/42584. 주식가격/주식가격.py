def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        sec = 0
        for j in range(i+1, len(prices)):
            if prices[j] >= prices[i]:
                sec += 1
            else:
                break
        answer.append(j - i)

    answer.append(0)
    return answer
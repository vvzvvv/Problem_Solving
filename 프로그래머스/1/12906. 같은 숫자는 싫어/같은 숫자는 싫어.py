def solution(arr):
    answer = []
    num = -1
    for i in arr:
        if num != i:
            answer.append(i)
            num = i
    return answer
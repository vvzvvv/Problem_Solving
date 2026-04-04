def solution(X, Y):
    x_arr = [0 for _ in range(10)]
    y_arr = [0 for _ in range(10)]
    
    for num in X:
        x_arr[int(num)] += 1
    for num in Y:
        y_arr[int(num)] += 1

    answer = ''
    for i in range(9, -1, -1):
        if x_arr[i] == 0 or y_arr[i] == 0: continue
        if x_arr[i] >= y_arr[i]:
            answer += str(i) * y_arr[i]
        else:
            answer += str(i) * x_arr[i]
    
    if answer == "": return "-1"
    if answer[0] == "0": return "0"
    return answer
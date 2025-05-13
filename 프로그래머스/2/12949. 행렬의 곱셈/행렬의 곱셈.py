def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    
    for x in range(len(arr1)):
        for b in range(len(arr2[0])):
            sum = 0
            
            for y in range(len(arr1[0])):
                sum += arr1[x][y] * arr2[y][b]
            
            answer[x][b] = sum
            
    return answer
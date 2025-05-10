def solution(n):
    answer = 0
    number = n ** 0.5
    if number == int(number):
        return (number + 1) ** 2
    else: 
        return -1
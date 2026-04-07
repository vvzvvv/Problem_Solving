def solution(ingredient):
    answer = 0
    ham = []
    for ing in ingredient:
        ham.append(ing)
        if len(ham) >= 4 and ham[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4): ham.pop()
    return answer
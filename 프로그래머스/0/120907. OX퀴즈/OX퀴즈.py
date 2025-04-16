def solution(quiz):
    answer = []
    for i in quiz:
        x, com, y, i, z = i.split()
        x = int(x)
        y = int(y)
        z = int(z)
        if (com == '-' and x - y == z) or (com == '+' and x + y == z):
            answer.append("O")
        else:
            answer.append("X")
        
    return answer
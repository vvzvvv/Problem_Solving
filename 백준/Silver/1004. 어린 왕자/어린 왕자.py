t = int(input())

for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split()) # 출발점, 도착점
    
    n = int(input())
    result = 0 # 행성계 진입/이탈 횟수
    for _ in range(n): 
        cx, cy, r = map(int, input().split()) #행성계 중점과 반지름
        if ((cx - x1) ** 2 + (cy - y1) ** 2 < r ** 2) and ((cx - x2) ** 2 + (cy - y2) ** 2 < r ** 2):
            continue
        elif ((cx - x1) ** 2 + (cy - y1) ** 2 < r ** 2) or ((cx - x2) ** 2 + (cy - y2) ** 2 < r ** 2):
            result += 1
    
    print(result)
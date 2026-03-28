def solution(rank, attendance):
    a, b, c = [-1, 101], [-1, 101], [-1, 101] #(번호, 등수)
    
    for num in range(len(rank)):
        if not attendance[num]: continue
        
        if rank[num] < a[1]:
            b, c = a[:], b[:]
            a = [num, rank[num]]
            
        elif rank[num] < b[1]:
            c = b[:]
            b = [num, rank[num]]
            
        elif rank[num] < c[1]:
            c = [num, rank[num]]
        
    return 10000 * a[0] + 100 * b[0] + c[0]
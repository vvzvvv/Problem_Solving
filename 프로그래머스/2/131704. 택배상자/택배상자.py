def solution(order):
    st = []
    i = 0
    
    for box in range(1, len(order) + 1):
        st.append(box)
        
        while st and st[-1] == order[i]:
            st.pop()
            i += 1
            
    return i
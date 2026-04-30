def solution(s):
    st = []
    for ch in s:
        if ch == '(':
            st.append(ch)
        elif ch ==')':
            if st and st[-1] == '(':
                st.pop()
            else:
                return False
    if st: return False
    return True
def to_min(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m

def solution(book_time):
    arr = [0]
    book_time.sort(key=lambda x: x[0])

    for start, end in book_time:
        n_st, n_ed = to_min(start), to_min(end)
        for i in range(len(arr)):
            if arr[i] <= n_st:
                arr[i] = n_ed + 10
                break
        else:
            arr.append(n_ed + 10)
        arr.sort()
            
    return len(arr)
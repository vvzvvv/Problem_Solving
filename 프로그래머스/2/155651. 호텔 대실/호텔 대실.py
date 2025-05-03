def to_minute(time):
    return int(time[:2]) * 60 + int(time[3:])

def solution(book_time):
    res = 0
    book_time.sort(key= lambda x: x[0])
    
    while book_time:
        room = []
        start, end = to_minute(book_time[0][0]), to_minute(book_time[0][1])
        room.append(0)
        
        for i in range(1, len(book_time)):
            new_start, new_end = to_minute(book_time[i][0]), to_minute(book_time[i][1])
            if end + 10 <= new_start:
                room.append(i)
                end = new_end
        
        for idx in reversed(room):
            book_time.pop(idx)
        
        res += 1
        
    return res
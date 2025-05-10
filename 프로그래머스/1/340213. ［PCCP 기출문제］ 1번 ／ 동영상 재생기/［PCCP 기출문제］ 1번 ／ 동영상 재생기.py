def to_sec(time):
    m, s = time.split(':')
    return int(m) * 60 + int(s)

def to_str(time):
    m = time // 60
    s = time % 60
    return f"{m:02d}:{s:02d}"


def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len = to_sec(video_len)
    op_start = to_sec(op_start)
    op_end = to_sec(op_end)
    pos = to_sec(pos)

    for com in commands:
        if op_start <= pos <= op_end:
            pos = op_end
        if com == "prev":
            pos -= 10
            if pos < 0:
                pos = 0
        elif com == "next":
            pos += 10
            if pos > video_len:
                pos = video_len
        
        if op_start <= pos <= op_end:
                pos = op_end
            
    return to_str(pos)
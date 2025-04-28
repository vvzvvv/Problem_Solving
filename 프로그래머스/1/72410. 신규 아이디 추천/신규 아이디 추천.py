def solution(new_id):
    # 1
    new_id = new_id.lower()
    # 2
    temp = ''
    for i in new_id:
        if i == '-' or i == '_' or i == '.' or 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57:
            temp += i
    new_id = temp
    # 3
    stack = ''
    for i in new_id:
        stack += i
        if stack[-2:] == '..':
            stack = stack[:-1]
    new_id = stack
    # 4
    if new_id[0] == '.':
        new_id = new_id[1:]
    if new_id[-1:] == '.':
        new_id = new_id[:-1]
    # 5
    if new_id == "": new_id = "a"
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    # 7
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]

    return new_id
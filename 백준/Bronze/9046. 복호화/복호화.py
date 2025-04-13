case = int(input())

for _ in range(case):
    word = input()
    arr = [0] * 26
    max_value = 0
    max_index = 0
    only_max = False
    for ch in word:
        # 공백이면 pass
        if ch == ' ': continue
    
        index = ord(ch) - 97
        arr[index] += 1
        # 등장 횟수가 max_value(맥스 등장횟수) 보다 크면 갱신
        if arr[index] > max_value:
            only_max = True  # 유일하게 가장 많이 등장
            max_value = arr[index]
            max_index = index
        elif arr[index] == max_value:
            only_max = False
            
    if only_max == False:
        print('?')
    
    else:
        max_word = chr(max_index + 97)
        print(max_word)
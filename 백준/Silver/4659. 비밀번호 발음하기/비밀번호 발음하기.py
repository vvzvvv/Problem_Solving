aeiou = ["a", "e", "i", "o", "u"]
    
while True:
    word = input()
    if word == "end": break

    flag = False
    # 모음 반드시 포함
    for w in word:
        if w in aeiou:
            flag = True
    
    if not flag:
        print("<{0}> is not acceptable.".format(word))
        continue
    
    # 모음 3개 연속, 자음 3개 연속 불가
    for i in range(len(word) - 2):
        자음, 모음 = 0, 0
        for w in word[i:i+3]:
            if w not in aeiou:
                자음 += 1
            else:
                모음 += 1
        if 자음 == 3 or 모음 == 3:
            flag = False
            break
    
    if not flag:
        print("<{0}> is not acceptable.".format(word))
        continue
    
    ## 같은 글자 2연속 X, ee/oo OK
    ok = ["ee", "oo"]
    for i in range(len(word)-1):
        if word[i] + word[i+1] in ok:
            continue
        if word[i] == word[i+1]:
            flag = False
            break
        
    if not flag:
        print("<{0}> is not acceptable.".format(word))
        continue
    else: print("<{0}> is acceptable.".format(word))
    
def solution(n, words):
    if len(words[0]) == 1: return [1, 1]
    
    d = {words[0]: 1}
    last = words[0][-1]
    cnt = 0
    
    for word in words[1:]:
        cnt += 1
        if len(word) == 1 or word in d or last != word[0]:
            break

        d[word] = 1
        last = word[-1]        
        if cnt == len(words) - 1: return [0, 0]
    
    return [cnt % n + 1, cnt // n + 1]
def solution(phone_book):
    dic = dict()
    for ph in phone_book:
        dic[ph] = 1
    
    for phone in phone_book:
        numbers = ''
        for i in range(len(phone) - 1):
            numbers += phone[i]
            if numbers in dic: return False
    
    return True
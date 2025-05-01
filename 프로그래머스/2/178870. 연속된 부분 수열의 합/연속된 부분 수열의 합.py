def solution(sequence, k):
    left = 0
    min_len = 1000000
    cur_sum = 0
    
    for right in range(len(sequence)):
        cur_sum += sequence[right]
        
        while cur_sum > k: # sum이 k보다 클 경우, 줄이기 -> left += 1
            cur_sum -= sequence[left]
            left += 1
            
        if cur_sum == k:
            if right - left < min_len:
                min_len = right - left
                result = [left, right]
    
    return result
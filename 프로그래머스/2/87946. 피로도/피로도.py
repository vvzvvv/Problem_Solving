from itertools import permutations

def solution(k, dungeons):
    answer = -1
    n = len(dungeons)
    
    for permutation in permutations(range(n), n):
        cnt, cur_k = 0, k
        for i in permutation:
            min_k, use_k = dungeons[i]
            if min_k > cur_k: continue
            cur_k -= use_k
            cnt += 1
            
        if cnt > answer:
            answer = cnt
            
    return answer
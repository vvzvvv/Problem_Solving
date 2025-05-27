from collections import deque

def check_one_diff(word1, word2):
    cnt = sum([1 for a, b in zip(word1, word2) if a != b])
    return cnt == 1

def solution(begin, target, words):
    if target not in words: return 0

    visited = [False] * len(words)
    queue = deque()
    queue.append((begin, 0))
    
    while queue:
        curr_word, total = queue.popleft()
        if curr_word == target:
            return total
        
        for i, word in enumerate(words):
            if not visited[i] and check_one_diff(curr_word, word):
                visited[i] = True
                queue.append((word, total + 1))
    
    return answer
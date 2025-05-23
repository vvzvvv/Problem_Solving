def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        stack = []
        for s in skill_tree:
            if s in skill:
                stack.append(s)
        
        if not stack:
            answer += 1
            continue
        
        idx = skill.index(stack[-1])
        if stack == list(skill[:idx+1]):
            answer += 1

    
    return answer
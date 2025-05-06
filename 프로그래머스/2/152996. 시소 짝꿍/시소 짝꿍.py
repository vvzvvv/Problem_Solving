from collections import Counter

def solution(weights):
    answer = 0
    count = Counter(weights)

    ratios = [(1, 1), (2, 3), (3, 4), (1, 2)]

    for w in count:
        for r1, r2 in ratios:
            target = w * r1 / r2
            if target in count:
                if target == w: # 자기 자신 조합
                    answer += count[w] * (count[w] - 1) // 2  
                else:
                    answer += count[w] * count[target]
    return answer

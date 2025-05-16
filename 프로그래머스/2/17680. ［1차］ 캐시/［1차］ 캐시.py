from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0 : return 5 * len(cities)
    answer = 0
    cities = [x.lower() for x in cities]
    cache = deque()
    
    for city in cities:
        if city not in cache:
            if len(cache) == cacheSize:
                cache.popleft()
                cache.append(city)
            else:
                cache.append(city)
            answer += 5
        elif city in cache:
            cache.remove(city) # 기존에 있던 거는 제거하고
            cache.append(city) # 최근 사용된 걸로 교체해 줘야함
            answer += 1
    return answer
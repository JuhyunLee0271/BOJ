from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
        
    for city in cities:
        # cache hit
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        # cache miss
        else:
            if cacheSize > 0:
                if len(cache) == cacheSize:
                    cache.popleft()
                    cache.append(city)
                else:
                    cache.append(city)
            answer += 5     
    
    return answer
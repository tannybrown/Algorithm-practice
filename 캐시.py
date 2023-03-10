def solution(cacheSize, cities):
    cache = []
    answer = 0
    
    
    if not cacheSize :
        return 5 * len(cities)
    
    for item in cities :
        item = item.lower()
        # 캐시가 안찼을때
        if len(cache) < cacheSize :
            if item in cache :
                answer += 1
                index = cache.index(item)
                cache.pop(index)
                cache.append(item)
            #miss
            else :
                answer += 5
                cache.append(item)
                
        #캐시 찼을때
        elif item in cache :
            answer += 1
            index = cache.index(item)
            cache.pop(index)
            cache.append(item)
            
        else : 
            answer += 5
            cache.pop(0)
            cache.append(item)
            
    
    return answer

def solution(n, words):
    lap = 1
    person = 2
    before = words[0]
    history = [before]
    
    for item in words[1:] :
        if before[-1] != item[0] :
            return [person,lap]
        else :
            if item in history :
                return [person,lap]
            else :
                before = item
                history.append(item)
                person += 1
                if person > n :
                    person = 1
                    lap += 1
    
    return [0,0]

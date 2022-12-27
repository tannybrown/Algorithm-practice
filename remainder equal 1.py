def solution(n):
    answer = 0
    n = n-1
    divider = 2
    if n % divider == 0 : answer = divider
    else : 
        divider += 1
        while 1 :
            if n % divider == 0 : 
                answer = divider
                break
            divider += 2
            
        
    
    return answer

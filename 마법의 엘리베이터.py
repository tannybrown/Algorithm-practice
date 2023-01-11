def solution(storey) :
    answer = 0
    i = 0
    while storey > 0 :
        modular = int(str(storey)[len(str(storey))- 1 - i])
        if modular > 5 :
            answer += (10 - modular)
            storey += (10 - modular) * pow(10,i)
        elif modular == 5 :
            #마지막입니까?
            if len(str(storey))- 1 == i:
                answer += 5
                storey -= modular * pow(10,i) 
            else :
                #앞의 숫자가 5이상 입니까? 
                if int(str(storey)[len(str(storey))- 2 - i]) >= 5:
                    answer += modular
                    storey += (10 - modular) * pow(10,i)
                else :
                    answer += modular
                    storey -= modular * pow(10,i)       
        else : 
            answer += modular
            storey -= modular * pow(10,i)
        i += 1        
    return answer

def solution(today, terms, privacies):
    answer = []
    pri_info = []
    
    #today 구조 분해
    year,month,day = today.split(".")
    today = [int(year),int(month),int(day)]
    
    #terms 구조 분해
    term = []
    for item in terms :
        kind, num = item.split(" ")
        num = int(num)
        term.append(kind)
        year1 = today[0]
        month1 = today[1] - num
        while month1 <= 0 :
            year1 -= 1
            month1 += 12
        term.append(year1)
        term.append(month1)  
        
        
    #privacies 구조 분해
    for item in range(len(privacies)) :
        days,kind = privacies[item].split(" ")
        year,month,day = days.split(".")
        year = int(year)
        month = int(month)
        day = int(day)
        
        for i in range(0,len(term),3) :
            if term[i] == kind :
                if year < term[i+1] :
                    answer.append(item+1)
                    break
                elif year == term[i+1] :
                    if month < term[i+2] :
                        answer.append(item+1)
                        break
                    elif month == term[i+2] and day <= today[2] :
                        answer.append(item+1)
                        break
        
    return answer

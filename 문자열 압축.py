import math

def solution(s):
    answer = 1001
    #길이 1인경우
    if len(s) == 1 :
        return 1
    
    #s 길이가 2이상인 경우
    for i in range(1,len(s) // 2 +1) :
        big =[]
        
        for j in range(len(s) // i):
            small = ""
            for k in range(i) :
                small += s[j*i +k]
            big.append(small)
        if len(s) % i != 0 :
            big.append(s[len(s)-(len(s)%i):])
        
        #counting section
        count = 1
        cur = 0
        for j in range(len(big)-1):
            if big[j] == big[j+1] :
                count+=1
            else : 
                if count >1 :
                    cur += i + len(str(count))
                else : 
                    cur += i
                count = 1
            #마지막 한번 더 체크   
        if count >1 :
            cur += i + len(str(count))
        else : 
            cur += i
        #딱 맞게 안잘렸을때 조정해주기
        if len(s) % i != 0 :
            cur -= (i - len(s)%i)
        
        #작은 값으로 answer 조정
        if answer > cur :
            answer = cur
        
    return answer

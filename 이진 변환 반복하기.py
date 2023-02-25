def solution(s):
    total_z = 0
    count = 0
    while s != "1" :
        zero = 0
        one = 0
        for item in s :
            if item == "0" :
                zero += 1
            elif item == "1" :
                one += 1
        total_z += zero
        count += 1
        s = str(bin(one)[2:])
    
        
    return [count,total_z]        
        

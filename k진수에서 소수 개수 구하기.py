import math
def solution(n, k):
    #진법 변환
    arr = []
    kstr = ""
    while n != 0 :
        a = n % k 
        n = n // k
        arr.append(a)
    kstr = ''.join(map(str, arr[::-1]))
    
    kstr = kstr.split("0")
    
    kstr = list(filter(lambda s: s != "" ,kstr))
    kstr = list(map(int,kstr))
    
    #counting
    count = 0
    correct = []
    def prime(num) :
        for i in range(2,int(math.sqrt(num))) :
            if num % i == 0 :
                return False
        return True
    
    for item in kstr :
        if item != 1 :
            if item in correct:
                count += 1
            elif int(math.sqrt(item)) == math.sqrt(item) :
                continue
            elif prime(item) :
                count += 1
                correct.append(item)
    return count
    
    
    

def solution(n,a,b):
    while n :
        # print(n ,a , b)
        half = n // 2
        q = 0
        w = 0
        if a <= half :
            q = 0
        else : 
            q = 1
        if b <= half :
            w = 0
        else :
            w = 1

        if q != w :
            ans = 0
            while n != 1 :
                n //= 2
                ans += 1
            return ans
        if q :
            a -= half
            b -= half
        
        n //= 2
        
# print(solution(16,2,3))

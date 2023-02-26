def solution(n):
    fibo0 = 0
    fibo1 = 1
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    for i in range(n-1) :
        temp = fibo1
        fibo1 = fibo0 + fibo1
        fibo0 = temp
    return fibo1 % 1234567
    
    return answer
